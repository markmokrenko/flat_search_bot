START_URL = 'https://www.sahibinden.com/kiralik-daire'
cities = {'Стамбул': '/istanbul'}
districts = {
    'Adalar': '-adalar?',
    'Arnavutköy': '-arnavutkoy?',
    'Ataşehir': '-atasehir?',
    'Avcılar': '-avcilar?',
    'Bağcılar': '-bagcilar?',
    'Bahçelievler': '-bahcelievler?',
    'Bakırköy': '-bakirkoy?',
    'Başakşehir': '-basaksehir?',
    'Bayrampaşa': '-bayrampasa?',
    'Beşiktaş': '-besiktas?',
    'Beykoz': '-beykoz?',
    'Beylikdüzü': '-beylikduzu?',
    'Beyoğlu': '-beyoglu?',
    'Büyükçekmece': '-buyukcekmece?',
    'Çatalca': '-catalca?',
    'Çekmeköy': '-cekmekoy?',
    'Esenler': '-esenler?',
    'Esenyurt': '-esenyurt?',
    'Eyüpsultan': '-eyupsultan?',
    'Fatih': '-fatih?',
    'Gaziosmanpaşa': '-gaziosmanpasa?',
    'Güngören': '-gungoren?',
    'Kadıköy': '-kadikoy?',
    'Kağıthane': '-kagithane?',
    'Kartal': '-kagithane?',
    'Küçükçekmece': '-kucukcekmece?',
    'Maltepe': '-maltepe?',
    'Pendik': '-pendik?',
    'Sancaktepe': '-sancaktepe?',
    'Sarıyer': '-sariyer?',
    'Şile': '-sile?',
    'Silivri': '-silivri?',
    'Şişli': '-sisli?',
    'Sultanbeyli': '-sultanbeyli?',
    'Sultangazi': '-sultangazi?',
    'Tuzla': '-tuzla?',
    'Ümraniye': '-umraniye?',
    'Üsküdar': '-uskudar?',
    'Zeytinburnu': '-zeytinburnu?'
}
rooms = {
    'Студия': 'a20=38472',
    'Однокомнатная': 'a20=38473&a20=1206094',
    'Двухкомнататная': 'a20=1213206&a20=38470&a20=1227923',
    'Трехкомнатная': 'a20=38496&a20=1259450&a20=38474',
    'Многокомнатная': 'a20=1227924&a20=38486&a20=1255142&a20=38471&a20=1227925&a20=38485&a20=217738&a20=38502&a20=38475&a20=1259969&a20=38479&a20=38494&a20=38497&a20=38477&a20=38480&a20=38500&a20=1256334&a20=38478&a20=38481&a20=38490&a20=38482&a20=38483&a20=1133410&a20=38498&a20=38491&a20=38492&a20=38493&a20=38487&a20=38488&a20=38489&a20=38501&a20=38495&a20=38476',
    'Неважно': ''
}
floors = {
    'Не нижний': 'a811=52042&a811=50278&a811=236072&a811=40708&a811=40986&a811=40592&a811=40593&a811=40594&a811=40595&a811=40596&a811=40597&a811=40598&a811=40599&a811=40600&a811=40601&a811=62364&a811=62365&a811=62366&a811=62367&a811=62368&a811=62369&a811=62370&a811=62371&a811=62372&a811=62373&a811=97308&a811=97309&a811=97310&a811=97311&a811=97312&a811=97313&a811=97314',
    'Неважно': ''
}
max_price = "&price_max="


async def create_url(state):
    list_url_components = []
    async with state.proxy() as data:
        list_url_components.append(cities[data['city']])
        list_url_components.append(districts[data['district']])
        list_url_components.append(rooms[data['rooms']])
        if data['rooms'] == 'Неважно':
            list_url_components.append('?' + floors[data['floor']])
        else:
            list_url_components.append('&' + floors[data['floor']])
        if data['rooms'] == 'Неважно' and data['floor'] == 'Неважно':
            list_url_components.append('?' + max_price + str(data['price']))
        else:
            list_url_components.append('&' + max_price + str(data['price']))
        return START_URL + ''.join(list_url_components)
