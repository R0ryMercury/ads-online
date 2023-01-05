from django.db import models

from users.models import User


class Ad(models.Model):
    title = models.CharField(
        max_length=200,
        verbose_name="Название товара",
        help_text="Укажите название товара",
    )
    price = models.PositiveIntegerField(
        verbose_name="Цена товара",
        help_text="Укажите цену товара",
    )
    description = models.TextField(
        max_length=2000,
        blank=True,
        null=True,
        verbose_name="Описание товара",
        help_text="Опишите свой товар",
    )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="ads",
        verbose_name="Автор объявления",
        help_text="Выберите автора объявления",
    )
    created_at = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(
        upload_to="images/",
        verbose_name="фото объявления",
        help_text="Загрузите фото для объявления",
        null=True,
        blank=True,
    )

    class Meta:
        verbose_name = "Объявление"
        verbose_name_plural = "Объявления"
        ordering = ["-price"]


class Comment(models.Model):
    text = models.TextField(
        max_length=1000,
        verbose_name="Комментарий",
        help_text="Оставить комментарий...",
    )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="comments",
        verbose_name="Автор комментария",
    )
    ad = models.ForeignKey(
        Ad,
        on_delete=models.CASCADE,
        related_name="comments",
        verbose_name="Объявление",
    )
    created_at = models.DateTimeField(auto_now_add=True)

    @property
    def author_image(self):
        return self.author.image if self.author.image else None

    class Meta:
        verbose_name = "Комментарий"
        verbose_name_plural = "Комментарии"
        ordering = ("-created_at",)
