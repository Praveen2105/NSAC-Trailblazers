from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import permissions
from rest_framework.views import APIView
from . import serializers
from . import models
from rest_framework import viewsets, status
from rest_framework.response import Response


# Create your views here.

def Home(request):
    return render(request, "index.html")
    # return redirect()


class ProfileViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.ProfileSerializer
    queryset = models.Profile.objects.all()

    def get_permissions(self):
        if self.action == 'list':
            permission_classes = [permissions.IsAuthenticated]
        else:
            permission_classes = [permissions.IsAdminUser]
        return [permission() for permission in permission_classes]

    def get_queryset(self, pk=None):
        if pk:
            profile = models.Profile.objects.get(id=pk)
        else:
            profile = models.Profile.objects.all()
        return profile

    def create(self, request, *args, **kwargs):
        data = request.data
        id = self.request.user.id
        user = models.Profile.objects.get(id=id)

        data['user'] = user.id
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def list(self, request, *arg, **kwargs):
        queryset = models.Profile.objects.all()
        serializer = serializers.ProfileSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class FireStationViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.FireStationSerializer

    def get_permissions(self):
        if self.action == 'list':
            permission_classes = [permissions.IsAuthenticated]
        else:
            permission_classes = [permissions.IsAdminUser]
        return [permission() for permission in permission_classes]

    def get_queryset(self, pk=None):
        if pk:
            firestation = models.FireStation.objects.get(id=pk)
        else:
            firestation = models.FireStation.objects.all()
        return firestation


class RescueCenterViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.RescueCenterSerializer

    def get_permissions(self):
        if self.action == 'list':
            permission_classes = [permissions.IsAuthenticated]
        else:
            permission_classes = [permissions.IsAdminUser]
        return [permission() for permission in permission_classes]

    def get_queryset(self, pk=None):
        if pk:
            rescuecenter = models.RescueCenter.objects.get(id=pk)
        else:
            rescuecenter = models.RescueCenter.objects.all()
        return rescuecenter


class UserReportViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.UserReportSerializer

    def get_permissions(self):
        if self.action == 'list':
            permission_classes = [permissions.IsAuthenticated]
        else:
            permission_classes = [permissions.IsAdminUser]
        return [permission() for permission in permission_classes]

    def get_queryset(self, pk=None):
        if pk:
            userreport = models.UserReport.objects.get(id=pk)
        else:
            userreport = models.UserReport.objects.all()
        return userreport

    def create(self, request, *args, **kwargs):
        data = request.data
        id = self.request.user.id
        user = models.Profile.objects.get(id=id)

        data['user'] = user.id
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


class DeviceReportViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.DeviceReportSerializer

    def get_permissions(self):
        if self.action == 'list':
            permission_classes = [permissions.IsAuthenticated]
        else:
            permission_classes = [permissions.IsAdminUser]
        return [permission() for permission in permission_classes]

    def get_queryset(self, pk=None):
        if pk:
            devicereport = models.DeviceReports.objects.get(id=pk)
        else:
            devicereport = models.DeviceReports.objects.all()
        return devicereport


class UserReportReviewViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.DeviceReportSerializer

    def get_permissions(self):
        if self.action == 'list':
            permission_classes = [permissions.IsAuthenticated]
        else:
            permission_classes = [permissions.IsAdminUser]
        return [permission() for permission in permission_classes]

    def get_queryset(self, pk=None):
        if pk:
            userreport = models.UserReportReview.objects.get(id=pk)
        else:
            userreport = models.UserReportReview.objects.all()
        return userreport
