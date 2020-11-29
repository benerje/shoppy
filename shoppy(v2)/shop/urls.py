from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="ShopHome"),
    path("about/", views.about, name="AboutUs"),
    path("contact/", views.contact, name="ContactUs"),
    path("search/", views.search, name="Search"),
    path("products/<int:myid>", views.productView, name="ProductView"),
    path("checkout/", views.checkout, name="CheckOut"),
    path("login/", views.loginPage, name="Login"),
    path("register/", views.registerPage, name="Register"),
    path("logout/", views.logoutUser, name="Logout"),
    path("orders/", views.orders, name="Orders"),
    path("dashboard/", views.dashboard, name="dashboard"),
]
