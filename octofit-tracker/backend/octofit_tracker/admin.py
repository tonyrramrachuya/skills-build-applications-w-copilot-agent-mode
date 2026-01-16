from django.contrib import admin
from .models import User, Team, Activity, Workout, Leaderboard

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
	list_display = ('username', 'email', 'team')

@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
	list_display = ('name',)

@admin.register(Activity)
class ActivityAdmin(admin.ModelAdmin):
	list_display = ('user', 'type', 'duration', 'distance')

@admin.register(Workout)
class WorkoutAdmin(admin.ModelAdmin):
	list_display = ('user', 'name')

@admin.register(Leaderboard)
class LeaderboardAdmin(admin.ModelAdmin):
	list_display = ('user', 'points')
