from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response
from rest_framework import status
import pandas as pd  # Import pandas

class ExcelUploadView(APIView):
    parser_classes = (MultiPartParser, FormParser)

    def post(self, request):
        file = request.data.get('file')
        if not file:
            return Response({'error': 'File not provided'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            # Use pandas to read the Excel file
            df = pd.read_excel(file)

            # Process and validate the data as needed
            # You can iterate through df rows and save them to the database
            for index, row in df.iterrows():
                # Perform validation and database insertion here

             return Response({'message': 'Data saved successfully'}, status=status.HTTP_201_CREATED)

        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
