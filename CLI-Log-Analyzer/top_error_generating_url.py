import top_requested_url

class TopErrorGeneratingURL(top_requested_url.TopRequestedURL):

    def __init__(self, file_path):
        self.file_path= file_path
        super().__init__(self.file_path)

    def import_data(self):
        super().import_data()

    def column_index(self):
        self.url_column_index = 0
        self.status_column_index = 0        
        for i in range(len(self.csv_data[0])):
            if (self.csv_data[0])[i] == 'url':
                self.url_column_index = i
                # print(url_column_index)
            elif (self.csv_data[0])[i]== 'status':
                self.status_column_index = i
        return self.url_column_index, self.status_column_index

    # Filtering URL which has error
    def filtering(self):
        
        error_url_count= {}
        unique_url= []
        self.csv_data.pop(0)         # removing header row
        url_error = [row[self.url_column_index] for row in self.csv_data if int(row[self.status_column_index])>=400]

        # inserting unique url
        for i in url_error:
            if i not in unique_url:
                unique_url.append(i)

        # making dictionary of count
        for url in unique_url:
            error_url_count[url]= url_error.count(url)

        self.top_error_generating_url = max(error_url_count.items(), key= lambda i: i[1])
        return self.top_error_generating_url

    def show_result(self):
        self.import_data()
        self.column_index()
        self.filtering()
        print(f'\nUrl that generate most error = {self.top_error_generating_url[0]}')
        print(f'And this url have generated error= {self.top_error_generating_url[1]} times')


# Tester code
a= TopErrorGeneratingURL('C:\Me\BSc\Self Initiated Projects\mini\log_analyser\Mini-Projects\CLI-Log-Analyzer\shorted_data.csv')
a.show_result()




