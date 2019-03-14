from django.shortcuts import render

posts = [
    {
        'title': 'التدوينة الأولى',
        'content': 'نص التدوينة الأولى كنص تجريبي',
        'post_date': '15-3-2019',
        'author': 'Ahmad Abouissa'
    },
    {
        'title': 'التدوينة الثانية',
        'content': 'نص التدوينة الثانية كنص تجريبي',
        'post_date': '20-3-2019',
        'author': 'Ali Khaled'
    },
    {
        'title': 'التدوينة الثالثة',
        'content': 'نص التدوينة الثالثة كنص تجريبي',
        'post_date': '28-3-2019',
        'author': 'Ahmad Abouissa'
    },
    {
        'title': 'التدوينة الرابعة',
        'content': 'نص التدوينة الرابعة كنص تجريبي',
        'post_date': '15-3-2019',
        'author': 'Mohamed Ali'
    },
]


def home(request):
    context = {
        'title': 'الصفحة الرئيسية',
        'posts': posts
    }
    return render(request, 'blog/index.html', context)


def about(request):
    return render(request, 'blog/about.html', {'title': 'من أنا'})
