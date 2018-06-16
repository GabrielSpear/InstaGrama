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
