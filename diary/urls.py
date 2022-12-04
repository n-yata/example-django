from django.urls import path
from .views import DiaryList,DiaryDetail,DiaryCreate,DiaryUpdate,DiaryDelete

urlpatterns = [
    path("", DiaryList.as_view(), name="diary_list"),
    path("detail/<int:pk>", DiaryDetail.as_view(), name="diary_detail"),
    path("create", DiaryCreate.as_view(), name="diary_create"),
    path("update/<int:pk>", DiaryUpdate.as_view(), name="diary_update"),
    path("delete/<int:pk>", DiaryDelete.as_view(), name="diary_delete"),
]