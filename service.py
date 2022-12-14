from getcon import GetConnection


class ServiceCategory:
    def service_test(self):
        getconn = GetConnection()
        getconn.getconnection()


service = ServiceCategory()
service.service_test()
