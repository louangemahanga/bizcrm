def user_role(request):
    if request.user.is_authenticated:
        is_manager = request.user.groups.filter(name='Manager').exists()
        is_commercial = request.user.groups.filter(name='Commercial').exists()
    else:
        is_manager = False
        is_commercial = False

    return {
        'is_manager':    is_manager,
        'is_commercial': is_commercial,
    }