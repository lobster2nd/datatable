import random
from datetime import timedelta

from django.http import JsonResponse
from django.shortcuts import render

from .models import Studies


def studies_list(request):
    start = int(request.GET.get('start', 0))             # pagination params
    length = int(request.GET.get('length', 10))

    search_value = request.GET.get('search[value]', '')  # filtration params
    search_type = request.GET.get('search[type]')        # search type

    studies = Studies.objects.select_related(
        'study_modality').prefetch_related('study_modality').values(
        'id',
        'patient_fio',
        'patient_birthdate',
        'study_uid',
        'study_date',
        'study_modality__name',
        'study_modality__short_code',
    )

    # filtration
    if search_value and search_type:
        if search_type == 'id':
            studies = studies.filter(id__icontains=search_value)
        elif search_type == 'patient_fio':
            studies = studies.filter(patient_fio__icontains=search_value)
        elif search_type == 'patient_birthdate':
            studies = studies.filter(patient_birthdate__icontains=search_value)
        elif search_type == 'study_date':
            studies = studies.filter(study_date__icontains=search_value)
        elif search_type == 'study_uid':
            studies = studies.filter(study_uid__icontains=search_value)
        elif search_type == 'study_name':
            studies = studies.filter(
                study_modality__name__icontains=search_value)
        elif search_type == 'study_short_code':
            studies = studies.filter(
                study_modality__short_code__icontains=search_value)

    # ordering
    order_by = request.GET.get('order_by')
    if order_by:
        if order_by == 'id':
            studies = studies.order_by('id')
        elif order_by == 'patient_fio':
            studies = studies.order_by('patient_fio')
        elif order_by == 'patient_birthdate':
            studies = studies.order_by('patient_birthdate')
        elif order_by == 'study_uid':
            studies = studies.order_by('study_uid')
        elif order_by == 'study_date':
            studies = studies.order_by('study_date')
        elif order_by == 'study_name':
            studies = studies.order_by('study_modality__name')
        elif order_by == 'study_short_code':
            studies = studies.order_by('study_modality__short_code')

    # pagination
    studies = studies[start:start + length]

    data = [
        {
            'id': s['id'],
            'patient_fio': s['patient_fio'],
            'patient_birthdate': s['patient_birthdate'],
            'study_uid': s['study_uid'],
            'study_date': s['study_date'],
            'study_name': s['study_modality__name'],
            'study_short_code': s['study_modality__short_code'],
        }
        for s in studies
    ]

    # receive records amount for server pagination
    total_records = Studies.objects.count()

    result = {
        'draw': int(request.GET.get('draw', 0)),
        'recordsTotal': total_records,
        'recordsFiltered': total_records,
        'data': data,
    }

    return JsonResponse(result)


def view_studies(request):
    return render(request, 'test_datatable/studies.html')


def random_date(start, end):
    """
    This function will return a random datetime between two datetime
    objects.
    """
    delta = end - start
    int_delta = (delta.days * 24 * 60 * 60) + delta.seconds
    random_second = random.randrange(int_delta)
    return start + timedelta(seconds=random_second)


def init_db(request):
    """
    База предоставляется уже предзаполненной, но в случае желания перехода
    на другую СУБД, можно раскомментировать код ниже и сгенерировать тестовые данные.
    """

    # Modalities.objects.all().delete()
    # modalities = [['CT', 'Computed Tomography'],
    #               ['MR', 'Magnetic Resonance'],
    #               ['PT', 'Positron emission tomography'],
    #               ['US', 'Ultrasound'],
    #               ['XA', 'X-Ray Angiography'],
    #               ['MG', 'Mammography'],
    #               ['CR', 'Computed Radiography'],
    #               ['AS', 'Angioscopy'],
    #               ['DX', 'Digital Radiography'],
    #               ['EC', 'Echocardiography']]
    # for modality in modalities:
    #     modality_obj = Modalities()
    #     modality_obj.short_code = modality[0]
    #     modality_obj.name = modality[1]
    #     modality_obj.save()
    # for i in range(100000):
    #     study_obj = Studies()
    #     study_obj.patient_fio = names.get_full_name()
    #     study_obj.patient_birthdate = random_date(datetime.datetime(2000, 1, 1, 0, 0, 0),
    #                                               datetime.datetime(2023, 1, 1, 0, 0, 0))
    #     study_obj.study_date = random_date(datetime.datetime(2023, 1, 1, 0, 0, 0),
    #                                        datetime.datetime(2023, 9, 1, 0, 0, 0))
    #     study_obj.study_uid = uuid.uuid4()
    #     random_modality_id = random.randint(1, 10)
    #     study_obj.study_modality = Modalities.objects.get(id=int(random_modality_id))
    #     study_obj.save()
    return render(request, 'test_datatable/init_db.html')
