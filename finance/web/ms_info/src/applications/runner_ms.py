from finance.web.ms_info.src.infrastructure.entry_points.route_rest import init_app


if __name__ == "__main__":
     app = init_app()
     app.run(debug=True)
