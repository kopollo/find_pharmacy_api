import argparse

import web_utils
from web_utils import geosearch_controller
from image_utils import show_image


def init_parser():
    parser = argparse.ArgumentParser(
        description="find organization on map ")

    parser.add_argument('--start_point', help="start search point")
    args = parser.parse_args()
    return args


def main():
    args = init_parser()

    org_to_search = 'аптека'
    start_point = args.start_point

    start_ll = geosearch_controller.get_ll_by_address(
        address=start_point,
    )
    org_points = geosearch_controller.generate_all_points(
        address=org_to_search,
        center=start_ll,
    )
    red = ',pm2rdl'
    for i in range(len(org_points)):

        org_points[i] += red
    # print(org_points, sep='\n')
    static_map_points = '~'.join(org_points)
    web_utils.generate_image(
        center_point=start_ll,
        map_type='map',
        points=static_map_points,
    )
    # show_image("map.png")
    # print(org_to_search, start_point, points)


if __name__ == '__main__':
    main()
