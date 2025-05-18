
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializer import EmployeeSerializers
from .models import Employee
from .decorators import log_execution

employee_buffer = []

@api_view(['POST'])
@log_execution
def receive_employee(request):
    serializer = EmployeeSerializers(data=request.data)
    if serializer.is_valid():
        employee_buffer.append(serializer.validated_data)

        if len(employee_buffer) >= 50:
            Employee.objects.bulk_create(
                [Employee(**data) for data in employee_buffer],
                ignore_conflicts=True
            )
            employee_buffer.clear()
        return Response({'status': 'received'})
    return Response(serializer.errors, status=400)


