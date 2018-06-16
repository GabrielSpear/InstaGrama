from django.shortcuts import render

# Create your views here.
# Login  function, display user profile function, displaying user_profile image, find_profile

@login_required(login_url='/accounts/login/')
def timelines(request):
    current_user = request.user
    images = Image.objects.order_by('-date_uploaded')
    profiles = Profile.objects.order_by('-last_update')
    comments = Comments.objects.order_by('-time_comment')
    return render(request, 'timelines.html', {'images': images, 'profiles': profiles, 'user_profile': user_profile, 'comments': comments})

@login_required(login_url='/accounts/login/')
def profile(request):
    current_user = request.user
    profile = Profile.objects.get(user_id=current_user)
    images = Image.objects.all().filter(user=current_user)
    return render(request, 'profile.html', {'images': images, 'profile': profile})

@login_required(login_url='/accounts/login/')
def new_status(request, username):
    current_user = request.user
    username = current_user.username
    if request.method == 'POST':
        form = NewStatusForm(request.POST, request.FILES)
        if form.is_valid():
            image = form.save()
            image.user = request.user
            image.save()
        return redirect('allTimelines')
    else:
        form = NewStatusForm()
    return render(request, 'new_status.html', {"form": form})

@login_required(login_url='/accounts/login')
def user_profile(request, user_id):
    profile = Profile.objects.get(id=user_id)
    images = Image.objects.all().filter(user_id=user_id)
    return render(request, 'profile.html', {'profile': profile, 'images': images})
