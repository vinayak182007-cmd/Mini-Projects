import top_requested_url

class Top_N_RequestedIp(top_requested_url.TopRequestedURL):

    def __init__(self, file_path, top_n):
        self.file_path= file_path
        self.top_n = top_n
        super().__init__(self.file_path)

    def import_data(self):
        super().import_data()

    def ip_column_index(self):
        self.ip_column= 0
        for i in range(len(self.csv_data[0])):
            if self.csv_data[0][i]=='ip':
                self.ip_column= i

    def processing_top_ips(self):
        self.csv_data.pop(0)

        # Intermediate data storage
        ip_count= {}
        unique_ip= []
        non_nnique_ip= []

        # Inserting data in intermediate data storage
        for row in self.csv_data:
            if row[self.ip_column] not in unique_ip:
                unique_ip.append(row[self.ip_column])
            else:
                non_nnique_ip.append(row[self.ip_column])

        all_ip= unique_ip + non_nnique_ip

        # Counting and finding top N ip requested
        for ip in unique_ip:
            ip_count[ip]= all_ip.count(ip)

        ip_sort= sorted(ip_count.items(), key= lambda i : i[1], reverse= True)
        top_requested_ips= ip_sort[0:self.top_n]

        return top_requested_ips   
    
    def show_results(self):
        self.import_data()
        self.ip_column_index()
        self.processing_top_ips()
        print(f'Top {self.top_n} requested ips are \n{self.processing_top_ips()}')
        

# tester code
# a= Top_N_RequestedIp('C:\Me\BSc\Self Initiated Projects\mini\log_analyser\Mini-Projects\CLI-Log-Analyzer\shorted_data.csv',2)
# print(a.show_results())