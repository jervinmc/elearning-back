from django.contrib import admin
from django.conf import settings
from django.urls import path
from django.urls.conf import include
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from users.views import Login,GetUserView,Signup
from classes.views import AdminViewClasses
from rest_framework import permissions
from classroomfiles.views import GetFileByProfID
from enrolled.views import viewByStudent,viewByCode,viewByStudentArchived,DeleteEnroll
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


urlpatterns = [
path('api/v1/admin/', admin.site.urls),
    path('api/v1/signup/', Signup.as_view(), name='Sign up'),
    path('api/v1/enrolled-student/', viewByStudent.as_view(), name='Sign up'),
    path('api/v1/enrolled-code/<str:code>/', viewByCode.as_view(), name='Sign up'),
    
    path('api/v1/classes-admin/', AdminViewClasses.as_view(), name='Sign up'),
    path('api/v1/enrolled-student-archived/', viewByStudentArchived.as_view(), name='Sign up'),
    
    path('api/v1/auth/login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/v1/auth/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/v1/auth/user/', GetUserView.as_view(), name='auth_data'),
    path('api/v1/classroomfiles-folderid/<str:folder_id>/', GetFileByProfID.as_view(), name='auth_data'),
    path('api/v1/login/', Login.as_view(), name='token_refresh'),
    path('api/v1/delete-enroll/', DeleteEnroll.as_view(), name='token_refresh'),
    path('api/v1/login/', Login.as_view(), name='token_refresh'),
    path('api/v1/classes/', include('classes.urls')),
    path('api/v1/classroomfiles/', include('classroomfiles.urls')),
    path('api/v1/folder/', include('classroomfolder.urls')),
    path('api/v1/localfiles/', include('localfiles.urls')),
    path('api/v1/notification/', include('notification.urls')),
    path('api/v1/todo/', include('todo.urls')),
    path('api/v1/users/', include('users.urls')),
    path('api/v1/enroll/', include('enrolled.urls')),
    
    # path('api/v1/users/details/', GetUserView.as_view(), name='get_user'),
]