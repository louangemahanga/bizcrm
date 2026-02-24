from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User, Group
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib import messages



def login_view(request):
    if request.user.is_authenticated:
        return redirect('crm:dashboard')

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('crm:dashboard')
        else:
            messages.error(request, '❌ Identifiants incorrects.')

    return render(request, 'users/login.html')


def logout_view(request):
    logout(request)
    return redirect('users:login')

def is_manager_or_admin(user):
    return user.is_superuser or user.groups.filter(name='Manager').exists()


@login_required
@user_passes_test(is_manager_or_admin)
def user_list(request):
    users = User.objects.all().prefetch_related('groups')
    return render(request, 'users/user_list.html', {'users': users})


@login_required
@user_passes_test(is_manager_or_admin)
def user_create(request):
    groups = Group.objects.all()
    if request.method == 'POST':
        username  = request.POST.get('username')
        email     = request.POST.get('email')
        password  = request.POST.get('password')
        group_id  = request.POST.get('group')

        if User.objects.filter(username=username).exists():
            messages.error(request, '❌ Ce nom d\'utilisateur existe déjà.')
        else:
            user = User.objects.create_user(username=username, email=email, password=password)
            if group_id:
                group = Group.objects.get(id=group_id)
                user.groups.add(group)
            messages.success(request, f'✅ Utilisateur {username} créé avec succès !')
            return redirect('users:user_list')

    return render(request, 'users/user_form.html', {'groups': groups})