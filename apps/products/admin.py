from django.contrib import admin

from .models import Banner, Brand, Category, Product, ProductImage


class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 1


@admin.register(Banner)
class BannerAdmin(admin.ModelAdmin):
    list_display = ["title", "subtitle", "order", "is_active"]
    list_editable = ["order", "is_active"]
    search_fields = ["title", "subtitle"]
    list_filter = ["is_active"]


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ["name", "slug", "icon", "order", "is_active"]
    list_editable = ["order", "is_active"]
    prepopulated_fields = {"slug": ("name",)}
    search_fields = ["name", "slug"]
    list_filter = ["is_active"]


@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    list_display = ["name", "country", "is_featured", "order", "is_active"]
    list_editable = ["order", "is_featured", "is_active"]
    prepopulated_fields = {"slug": ("name",)}
    search_fields = ["name", "country"]
    list_filter = ["is_featured", "is_active"]


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = [
        "name", "brand", "category", "product_type",
        "price", "in_stock", "is_featured", "created_at",
    ]
    list_editable = ["in_stock", "is_featured"]
    list_filter = ["category", "brand", "product_type", "skin_type", "in_stock", "is_featured"]
    search_fields = ["name", "description", "brand__name"]
    readonly_fields = ["created_at", "updated_at"]
    date_hierarchy = "created_at"
    inlines = [ProductImageInline]
