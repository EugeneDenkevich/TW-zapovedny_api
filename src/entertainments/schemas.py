from config.utils.schemas import BasicAPISchema

from .serializers import (
    EntertainmentSerializer,
    ExcursionSerializer,
)


class EntertainmentsSchema(BasicAPISchema):

    def retrieve(self):
        return self.extend_schema(
            description='Get entertainment by id',
            summary='Get entertainment by id',
            request=EntertainmentSerializer,
            responses={
                200: EntertainmentSerializer,
                **self.get_responses(404)
            }
        )

    def list(self):
        return self.extend_schema(
            description='Get entertainments',
            summary='Get entertainments',
            request=EntertainmentSerializer,
            responses={200: EntertainmentSerializer}
        )


class ExcursionsSchema(BasicAPISchema):

    def retrieve(self):
        return self.extend_schema(
            description='Get excursion by id',
            summary='Get excursion by id',
            request=ExcursionSerializer,
            responses={200: ExcursionSerializer, **self.get_responses(404)}
        )

    def list(self):
        return self.extend_schema(
            description='Get excursions',
            summary='Get excursions',
            request=ExcursionSerializer,
            responses={200: ExcursionSerializer}
        )

class GalerySchema(BasicAPISchema):
    
    def list(self):
        return self.extend_schema(
            summary='Get galeries',
            description='Get galeries',
        )
    

class NearestSchema(BasicAPISchema):
    
    def list(self):
        return self.extend_schema(
            summary='Get nearesrs',
            description='Get nearesrs',
        )


entertainment_schema = EntertainmentsSchema(tags=['Entertainment'])
excursion_schema = ExcursionsSchema(tags=['Excursions'])
galery_schema = GalerySchema(tags=['Galery'])
nearest_schema = NearestSchema(tags=['Nearests Places'])
