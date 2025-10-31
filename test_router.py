from router import Router

routes = [
    ("223.1.1.0/24", "Link 0"),
    ("223.1.2.0/24", "Link 1"),
    ("223.1.3.0/24", "Link 2"),
    ("223.1.0.0/16", "Link 4 (ISP)")
]

r = Router(routes)

print(r.route_packet("223.1.1.100"))  # Link 0
print(r.route_packet("223.1.2.5"))    # Link 1
print(r.route_packet("223.1.250.1"))  # Link 4 (ISP)
print(r.route_packet("198.51.100.1")) # Default Gateway