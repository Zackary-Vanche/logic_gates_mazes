def point_in_polygon(point, polygon_points):
    """ Vérifie si un point est à l'intérieur d'un polygone en utilisant l'algorithme du rayon """
    x, y = point
    n = len(polygon_points)
    inside = False
    p1x, p1y = polygon_points[0]
    for i in range(n + 1):
        p2x, p2y = polygon_points[i % n]
        if y > min(p1y, p2y):
            if y <= max(p1y, p2y):
                if x <= max(p1x, p2x):
                    if p1y != p2y:
                        xinters = (y - p1y) * (p2x - p1x) / (p2y - p1y) + p1x
                    if p1x == p2x or x <= xinters:
                        inside = not inside
        p1x, p1y = p2x, p2y
    return inside

def point_in_ellipse(point, ellipse_rect):
    """ Vérifie si un point est à l'intérieur d'une ellipse définie par un Rect """
    cx = ellipse_rect.x + ellipse_rect.width / 2  # Centre x de l'ellipse
    cy = ellipse_rect.y + ellipse_rect.height / 2  # Centre y de l'ellipse
    rx = ellipse_rect.width / 2  # Rayon x de l'ellipse
    ry = ellipse_rect.height / 2  # Rayon y de l'ellipse
    px, py = point  # Point de clic
    # Formule de l'ellipse : ((x - cx)^2 / rx^2) + ((y - cy)^2 / ry^2) <= 1
    return ((px - cx) ** 2) / (rx ** 2) + ((py - cy) ** 2) / (ry ** 2) <= 1