from .main import Note


def test_ajout():

  note = Note('xx', 'yy', 'zzz')
  print(note)

  Note.vider()
  assert len(Note.instances) == 0
  Note(eleve = 'eleve1', matiere='math', valeur=12)
  assert len(Note.instances) == 1