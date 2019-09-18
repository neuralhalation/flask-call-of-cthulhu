def add_points(current_total, points_added, max_possible):
    if current_total + points_added > max_possible:
        return max_possible
    else:
        return current_total + points_added


def subtract_points(current_total, points_subtracted, min_possible):
    if current_total - points_subtracted < min_possible:
        return min_possible
    else:
        return current_total - points_subtracted
