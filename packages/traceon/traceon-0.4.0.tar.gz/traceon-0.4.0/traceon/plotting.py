"""The `traceon.plotting` module uses the `vedo` plotting library to provide some convenience functions
to show the line and triangle meshes generated by Traceon."""

from math import sqrt
from scipy.interpolate import *
import numpy as np
import vedo

from . import backend
from .geometry import Symmetry

def _create_point_to_physical_dict(mesh):
    d = {}

    for k, v in mesh.physical_to_elements.items():
        for elm in v:
            for p in mesh.elements[elm]:
                d[p] = k
    
    return d


def plot_mesh(mesh, *args, **kwargs):
     
    if mesh.symmetry == Symmetry.RADIAL:
        return plot_line_mesh(mesh, *args, **kwargs)
    elif mesh.symmetry == Symmetry.THREE_D_HIGHER_ORDER or Symmetry.THREE_D:
        return plot_triangle_mesh(mesh, *args, **kwargs)

def plot_charge_density(excitation, field, *args, **kwargs):
    
    mesh = excitation.mesh 
    
    if mesh.symmetry == Symmetry.RADIAL:
        return _plot_charge_density_2d(excitation, field, *args, **kwargs)
    elif mesh.symmetry == Symmetry.THREE_D_HIGHER_ORDER:
        return _plot_charge_density_3d(excitation, field, *args, **kwargs)

def _plot_charge_density_3d(excitation, field, density=False):
    
    all_vertices, name = excitation.get_active_elements()
    
    if density:
        all_charges = field.charges
    else:
        all_charges = np.array([field.charge_on_element(i) for i in range(len(all_vertices))])
    
    charge_min, charge_max = np.min(all_charges), np.max(all_charges)
    
    plotter = vedo.Plotter()

    for _, indices in name.items():
        vertices = all_vertices[indices, :3]
        
        points = np.reshape(vertices, (3*len(vertices), 3))
        p_indices = np.arange(3*len(vertices)).reshape( (len(vertices), 3) )
        vm = vedo.Mesh([points, p_indices])
        vm.linecolor('black').linewidth(2)
        
        vm.cellcolors = 255*vedo.colors.color_map(all_charges[indices], name='jet', vmin=charge_min, vmax=charge_max)
        plotter.add(vm)
    
    plotter.show(viewup='z', axes={'xtitle': 'x (mm)', 'ytitle': 'y (mm)', 'ztitle': 'z (mm)'})

def _plot_charge_density_2d(excitation, field, density=False):
    all_vertices, name = excitation.get_active_elements()
    all_charges = np.array([field.charge_on_element(i) for i in range(len(all_vertices))])
    
    if density:
        lengths = np.linalg.norm(all_vertices[:, 1] - all_vertices[:, 0])
        all_charges /= lengths
    
    assert len(all_vertices) == len(all_charges)
    charge_min, charge_max = np.min(all_charges), np.max(all_charges)
    
    plotter = vedo.Plotter()
    
    for _, indices in name.items():
        vertices = all_vertices[indices]
        start_points = np.reshape(np.array( [(P1, P3, P4) for P1,_,P3,P4 in vertices] ), (len(vertices)*3, 3))
        end_points = np.reshape(np.array([(P3, P4, P2) for _,P2,P3,P4 in vertices]), (len(vertices)*3, 3))
        l = vedo.Lines(start_points, end_points, lw=3)
        colors = np.repeat(all_charges[indices], 6)
        l.cmap('jet', colors, vmin=charge_min, vmax=charge_max)
        plotter.add(l)
    
    plotter.show(axes={'xtitle': 'x (mm)', 'ytitle': 'y (mm)'})
    
    

def plot_triangle_mesh(mesh, show_legend=True, show_normals=False, **phys_colors):
    
    triangles = mesh.elements
     
    triangles_to_plot = []
    normals = []
    
    if mesh.symmetry == Symmetry.THREE_D:
        triangles_to_plot = np.copy(triangles)
        normals = [backend.normal_3d(*mesh.points[t]) for t in triangles]
    elif mesh.symmetry == Symmetry.THREE_D_HIGHER_ORDER:
        normal_coordinates = [(1/6, 1/6), (1/2-1/6, 1/2-1/6), (1/2-1/6, 1/6), (1/6, 1/2-1/6)]
        for (v0, v1, v2, v3, v4, v5) in triangles:
            for i, (A, B, C) in enumerate([(v0, v3, v5), (v3, v4, v5), (v3, v1, v4), (v5, v4, v2)]):
                triangles_to_plot.append( [A, B, C] )
                alpha, beta = normal_coordinates[i]
                normals.append(backend.higher_order_normal_3d(alpha, beta, mesh.points[[v0, v1, v2, v3, v4, v5]]))
     
    normals, triangles_to_plot = np.array(normals), np.array(triangles_to_plot)
     
    # Calculate color per triangle
    # If all three vertices of a triangle belong to a physical group, the triangle
    # receives the color of the physical group
    colors = np.full(len(triangles_to_plot), '#CCCCCC')
    dict_ = _create_point_to_physical_dict(mesh)
    
    for i, (A, B, C) in enumerate(triangles_to_plot):
        if A in dict_ and B in dict_ and C in dict_:
            phys1, phys2, phys3 = dict_[A], dict_[B], dict_[C]
            if phys1 == phys2 and phys2 == phys3 and phys1 in phys_colors:
                colors[i] = phys_colors[phys1]
     
    plotter = vedo.Plotter()
    meshes = []
    
    for c in set(colors):
        mask = colors == c
        vm = vedo.Mesh([mesh.points, triangles_to_plot[mask]], c)
        vm.linecolor('black').linewidth(2)
        
        key = [k for k, col in phys_colors.items() if c==col]
        if len(key):
            vm.legend(key[0])
        
        plotter += vm
        meshes.append(vm)
    
    if show_normals:
        start_to_end = np.zeros( (len(triangles_to_plot), 6) )
        for i, t in enumerate(triangles_to_plot):
            v1, v2, v3 = mesh.points[t]
            middle = (v1 + v2 + v3)/3
            area = 1/2*np.linalg.norm(np.cross(v2-v1, v3-v1))
            side_length = sqrt( (4*area) / sqrt(3) ) # Equilateral triangle, side length with equal area
            normal = 0.75*side_length*normals[i]
            start_to_end[i] = [*middle, *(middle+normal)]
         
        arrows = vedo.shapes.Arrows(start_to_end[:, :3], start_to_end[:, 3:], res=20, c='black')
        plotter.add(arrows)
     
    lb = vedo.LegendBox(meshes)
    plotter.add(lb)
     
    plotter.show(viewup='z', axes={'xtitle': 'x (mm)', 'ytitle': 'y (mm)', 'ztitle': 'z (mm)'})


def plot_line_mesh(mesh, show_legend=True, show_normals=False, **colors):
    """Show a 2D mesh (mesh consisting of many line elements).
    
    Parameters
    ---------
    mesh: meshio object
        The mesh to show.
    show_legend: bool
        Whether to show a legend. The colors in the legend will correspond to the different physical
        groups present in the geometry.
    colors: dict
        The colors to use for the physical groups. The keys in the dictionary correspond to the
        physical group names, while the values can be any color understood by vedo.
    """
    dict_ = _create_point_to_physical_dict(mesh)
    lines = mesh.elements
     
    start = []
    end = []
    colors_ = []
    normals = []
    
    for (P1, P2, P3, P4) in lines:
        for i, (A, B) in enumerate([(P1, P3), (P3, P4), (P4, P2)]):
            color = '#CCCCC'

            if A in dict_ and B in dict_:
                phys1, phys2 = dict_[A], dict_[B]
                if phys1 == phys2 and phys1 in colors:
                    color = colors[phys1]
            
            p1, p2 = mesh.points[A], mesh.points[B]
            start.append(p1)
            end.append(p2)
            colors_.append(color)
            normals.append(backend.higher_order_normal_radial(-2/3 + i*2/3, mesh.points[np.array([P1, P2, P3, P4])]))
    
    start, end = np.array(start), np.array(end)
    colors_ = np.array(colors_)
    plotter = vedo.Plotter()
    lines = []
     
    for c in set(colors_):
        mask = colors_ == c
        l = vedo.Lines(start[mask], end[mask], lw=3, c=c)
        
        key = [k for k, col in colors.items() if c==col]
        if len(key):
            l.legend(key[0])
         
        plotter += l
        lines.append(l)
    
    lb = vedo.LegendBox(lines)
    plotter += lb
    
    if show_normals:
        arrows_to_plot = np.zeros( (len(normals), 4) )
        
        for i, (v1, v2) in enumerate(zip(start, end)):
            v1, v2 = v1[:2], v2[:2]
            middle = (v1 + v2)/2
            length = np.linalg.norm(v2-v1)
            normal = 3*length*normals[i]
            arrows_to_plot[i] = [*middle, *(middle+normal)]
        
        arrows = vedo.shapes.Arrows(arrows_to_plot[:, :2], arrows_to_plot[:, 2:], c='black')
        plotter.add(arrows)
    
    plotter.show(axes={'xtitle': 'x (mm)', 'ytitle': 'y (mm)'})

'''
def show_charge_density(lines, charges):
    # See https://matplotlib.org/stable/gallery/lines_bars_and_markers/multicolored_line.html
    assert len(lines) == len(charges)

    plt.figure()
    segments = lines[:, :, :2] # Remove z value
    
    amplitude = np.mean(np.abs(charges))
    norm = plt.Normalize(-3*amplitude, 3*amplitude)
    
    lc = LineCollection(segments, cmap='coolwarm', norm=norm)
    lc.set_array(charges)
    lc.set_linewidth(4)
    line = plt.gca().add_collection(lc)
    plt.xlim(np.min(lines[:, :, 0])-0.2, np.max(lines[:, :, 0])+0.2)
    plt.ylim(np.min(lines[:, :, 1])-0.2, np.max(lines[:, :, 1])+0.2)
    plt.xlabel('r (mm)')
    plt.ylabel('z (mm)')
    plt.show()
'''


