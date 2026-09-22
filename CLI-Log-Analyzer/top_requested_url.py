import csv

class TopRequestedURL:

    def __init__(self, file_path):
        self.file_path = file_path
        self.csv_data = []
        self.url_column = 0

    def import_data(self):
        with open(str(self.file_path), 'r') as file:
            csv_data = csv.reader(file)
            for row in csv_data:
                self.csv_data.append(row)

    def select_url_column(self):
        self.url_column = 0
        for i in range(len(self.csv_data[0])):
            if self.csv_data[0][i] == 'url':
                self.url_column = i
                break
        return self.url_column

    def get_top_requested_url(self):
        self.url_count = {}
        unique_urls = []
        url_column_data = [row[self.url_column] for row in self.csv_data[1:]]
        for url in url_column_data:
            if url not in unique_urls:
                unique_urls.append(url)
        for url in unique_urls:
            self.url_count[url] = url_column_data.count(url)
        top_requested_url = max(self.url_count, key=self.url_count.get)
        return top_requested_url

    def fetch_top_requested_url(self):
        self.import_data()
        self.select_url_column()
        top_requested_url = self.get_top_requested_url()
        print(f'Top requested URL: {top_requested_url}')
        print(f'Number of times top requested URL was requested: {self.url_count.get(top_requested_url)}')

# Tester code
# data_analysis_1 = TopRequestedURL('C:\Me\BSc\Self Initiated Projects\mini\log_analyser\Mini-Projects\CLI-Log-Analyzer\shorted_data.csv')
# data_analysis_1.fetch_top_requested_url()


