
def get_frailejon_regions():
    """
    Returns a list of páramo regions with frailejón data in Colombia.
    
    This is a data source for the map visualization that shows páramos
    and their frailejón populations in Colombia.
    """
    # Data about Colombian páramos and their frailejón populations
    # This dataset focuses on the most important páramos for water regulation and biodiversity
    paramos = [
        {
            "name": "Páramo de Sumapaz",
            "lat": 4.1167,
            "lon": -74.1167,
            "department": "Cundinamarca/Meta",
            "risk": "Alto",
            "frailejon_density": 85,
            "area": 2662,
            "altitude": 3500,
            "ecosystem_services": "Regulación hídrica, captura de carbono, biodiversidad",
            "description": "El páramo más grande del mundo, fundamental para el abastecimiento de agua de Bogotá"
        },
        {
            "name": "Páramo de Chingaza",
            "lat": 4.5167,
            "lon": -73.7667,
            "department": "Cundinamarca/Meta",
            "risk": "Alto",
            "frailejon_density": 90,
            "area": 766,
            "altitude": 3800,
            "ecosystem_services": "Abastecimiento hídrico, conservación de especies endémicas",
            "description": "Principal fuente de agua para Bogotá, con poblaciones densas de frailejones"
        },
        {
            "name": "Páramo de Santurbán",
            "lat": 7.2833,
            "lon": -72.8333,
            "department": "Santander/Norte de Santander",
            "risk": "Crítico",
            "frailejon_density": 45,
            "area": 142,
            "altitude": 3200,
            "ecosystem_services": "Regulación hídrica, biodiversidad endémica",
            "description": "Amenazado por actividades mineras, pérdida significativa de frailejones"
        },
        {
            "name": "Páramo de Guerrero",
            "lat": 5.1667,
            "lon": -73.8333,
            "department": "Cundinamarca",
            "risk": "Alto",
            "frailejon_density": 70,
            "area": 387,
            "altitude": 3400,
            "ecosystem_services": "Regulación hídrica, conservación de flora endémica",
            "description": "Presión por expansión urbana y actividades agropecuarias"
        },
        {
            "name": "Páramo de Rabanal",
            "lat": 5.3333,
            "lon": -73.3333,
            "department": "Boyacá/Cundinamarca",
            "risk": "Medio",
            "frailejon_density": 75,
            "area": 455,
            "altitude": 3600,
            "ecosystem_services": "Regulación hídrica, captura de carbono",
            "description": "Estado de conservación moderado con poblaciones estables de frailejones"
        },
        {
            "name": "Páramo de Pisba",
            "lat": 5.7167,
            "lon": -72.4333,
            "department": "Boyacá/Casanare",
            "risk": "Medio",
            "frailejon_density": 80,
            "area": 1118,
            "altitude": 3700,
            "ecosystem_services": "Biodiversidad, regulación climática",
            "description": "Uno de los páramos mejor conservados de Colombia"
        },
        {
            "name": "Páramo de Almorzadero",
            "lat": 7.0833,
            "lon": -72.8667,
            "department": "Santander/Norte de Santander",
            "risk": "Alto",
            "frailejon_density": 55,
            "area": 177,
            "altitude": 3300,
            "ecosystem_services": "Regulación hídrica, biodiversidad",
            "description": "Degradación moderada por actividades humanas"
        },
        {
            "name": "Páramo de Cocuy",
            "lat": 6.5000,
            "lon": -72.3167,
            "department": "Boyacá/Arauca/Casanare",
            "risk": "Bajo",
            "frailejon_density": 95,
            "area": 3063,
            "altitude": 4000,
            "ecosystem_services": "Glaciares, biodiversidad única, regulación hídrica",
            "description": "Excelente estado de conservación, poblaciones densas de frailejones gigantes"
        },
        {
            "name": "Páramo de Los Nevados",
            "lat": 4.8833,
            "lon": -75.3667,
            "department": "Caldas/Risaralda/Quindío/Tolima",
            "risk": "Medio",
            "frailejon_density": 85,
            "area": 583,
            "altitude": 3900,
            "ecosystem_services": "Turismo ecológico, regulación hídrica, biodiversidad",
            "description": "Área protegida con buena conservación de frailejones"
        },
        {
            "name": "Páramo de Puracé",
            "lat": 2.3167,
            "lon": -76.4000,
            "department": "Cauca/Huila",
            "risk": "Medio",
            "frailejon_density": 78,
            "area": 835,
            "altitude": 3600,
            "ecosystem_services": "Biodiversidad volcánica, regulación hídrica",
            "description": "Ecosistema volcánico con especies endémicas de frailejones"
        },
        {
            "name": "Páramo de Frontino",
            "lat": 6.1667,
            "lon": -76.1167,
            "department": "Antioquia",
            "risk": "Alto",
            "frailejon_density": 60,
            "area": 123,
            "altitude": 3200,
            "ecosystem_services": "Regulación hídrica local, biodiversidad",
            "description": "Presión por minería aurífera y expansión agrícola"
        },
        {
            "name": "Páramo de Belmira",
            "lat": 6.6167,
            "lon": -75.6667,
            "department": "Antioquia",
            "risk": "Alto",
            "frailejon_density": 50,
            "area": 195,
            "altitude": 3100,
            "ecosystem_services": "Abastecimiento hídrico regional",
            "description": "Fragmentación del hábitat por actividades humanas"
        },
        {
            "name": "Páramo de Sonsón",
            "lat": 5.7167,
            "lon": -75.3000,
            "department": "Antioquia",
            "risk": "Medio",
            "frailejon_density": 72,
            "area": 167,
            "altitude": 3400,
            "ecosystem_services": "Conservación de especies, regulación hídrica",
            "description": "Estado de conservación moderado con iniciativas locales"
        },
        {
            "name": "Páramo de Tamá",
            "lat": 7.4333,
            "lon": -72.3833,
            "department": "Norte de Santander",
            "risk": "Bajo",
            "frailejon_density": 88,
            "area": 518,
            "altitude": 3500,
            "ecosystem_services": "Conectividad binacional, biodiversidad única",
            "description": "Parque Nacional Natural con excelente conservación transfronteriza"
        },
        {
            "name": "Páramo de Bordoncillo",
            "lat": 0.8333,
            "lon": -77.6333,
            "department": "Nariño",
            "risk": "Medio",
            "frailejon_density": 82,
            "area": 445,
            "altitude": 3800,
            "ecosystem_services": "Biodiversidad andina, regulación climática",
            "description": "Páramo meridional con especies únicas de frailejones"
        },
        {
            "name": "Páramo de Paja Blanca",
            "lat": 5.0000,
            "lon": -74.6667,
            "department": "Cundinamarca",
            "risk": "Alto",
            "frailejon_density": 65,
            "area": 234,
            "altitude": 3300,
            "ecosystem_services": "Abastecimiento hídrico, captura de carbono",
            "description": "Presión urbana de la sabana de Bogotá"
        },
        {
            "name": "Páramo de Cruz Verde",
            "lat": 4.6000,
            "lon": -73.9833,
            "department": "Cundinamarca",
            "risk": "Alto",
            "frailejon_density": 68,
            "area": 189,
            "altitude": 3450,
            "ecosystem_services": "Regulación hídrica para Bogotá",
            "description": "Cercanía a zonas urbanas genera presión sobre el ecosistema"
        },
        {
            "name": "Páramo de Tota",
            "lat": 5.5667,
            "lon": -72.9167,
            "department": "Boyacá",
            "risk": "Alto",
            "frailejon_density": 55,
            "area": 278,
            "altitude": 3015,
            "ecosystem_services": "Lago de alta montaña, biodiversidad acuática",
            "description": "Presión por agricultura intensiva y contaminación del lago"
        }
    ]
    
    return paramos

def get_risk_regions():
    """
    Función de compatibilidad que redirige a get_frailejon_regions()
    """
    return get_frailejon_regions()
