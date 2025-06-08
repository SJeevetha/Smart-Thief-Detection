def format_thief_info(thief):
    return f"Name: {thief['name']}, Area: {thief['area']}"

if __name__ == "__main__":
    thief = {'name': 'John Doe', 'area': 'Downtown'}
    print(format_thief_info(thief))
