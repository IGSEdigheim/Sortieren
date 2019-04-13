import pprint


def selection_sort(A, col):
    n = len(A)
    for i in range(0, n-1):
        kleinste = i
        for j in range(i+1, n):
            if A[j][col] < A[kleinste][col]:
                kleinste = j
        A[kleinste], A[i] = A[i], A[kleinste]
    return A


listeDaten = [
    ('Bergmann', 'Laura', 'Schmarjestrasse 76', '93497', 'Willmering'),
    ('Brandt', 'Mandy', 'Scharnweberstrasse 84', '68199', 'Mannheim Almenhof'),
    ('Ebersbacher', 'Michelle', 'Alt-Moabit 10', '06691', 'Zeitz'),
    ('Frey', 'Kristian', 'Hans-Grade-Allee 7', '24870', 'Ellingstedt'),
    ('Gruenewald', 'Marco', 'Nuernbergerstrasse 15', '26386', 'Wilhelmshaven'),
    ('Herzog', 'Marco', 'Scharnweberstrasse 90', '61130', 'Nidderau'),
    ('Keller', 'Christina', 'Alt Reinickendorf 24', '87542', 'Blaichach'),
    ('Koertig', 'Christine', 'Hardenbergstraße 82', '66887', 'Niederalben'),
    ('Kortig', 'Stefanie', 'Mühlenstrasse 76', '97201', 'Höchberg'),
    ('Krause', 'Stefanie', 'Brandenburgische Str. 20', '74343', 'Sachsenheim'),
    ('Loewe', 'Ulrike', 'Messedamm 69', '06054', 'Halle'),
    ('Mahler', 'Sophia', 'Charlottenstrasse 87', '01463', 'Langebrück'),
    ('Meister', 'Stephan', 'Fasanenstrasse 17', '22605', 'Hamburg Othmarschen'),
    ('Möller', 'Jens', 'Schoenebergerstrasse 47', '08313', 'Bernsbach'),
    ('Nussbaum', 'Florian', 'Kurfürstendamm 56', '08004', 'Zwickau'),
    ('Reinhard', 'Kevin', 'An Der Urania 15', '25856', 'Hattstedt'),
    ('Schmidt', 'Vanessa', 'Paderborner Strasse 44', '86359', 'Gersthofen'),
    ('Schmitz', 'Andreas', 'Meininger Strasse 84', '66539', 'Neunkirchen Ludwigsthal'),
    ('Schreiber', 'Barbara', 'Stresemannstr. 56', '66592', 'St Wendel'),
    ('Schulz', 'Alexander', 'Anhalter Strasse 45', '67744', 'Seelen')
    ]

pp = pprint.PrettyPrinter(compact=True)
pp.pprint(selection_sort(listeDaten, 3))