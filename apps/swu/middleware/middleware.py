from django.utils.deprecation import MiddlewareMixin
import logging

logger = logging.getLogger(__name__)


class StoreRequestsMiddleware(MiddlewareMixin):

    def process_request(self, request):

        response = self.get_response(request)
        msg = '{} | {} | {}'.format(request.get_raw_uri(), request.method, request.path)
        logger.info(msg)

        return response
