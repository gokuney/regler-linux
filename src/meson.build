pkgdatadir = join_paths(get_option('prefix'), get_option('datadir'), meson.project_name())
moduledir = join_paths(pkgdatadir, 'regler')
gnome = import('gnome')

gnome.compile_resources('regler',
  'regler.gresource.xml',
  gresource_bundle: true,
  install: true,
  install_dir: pkgdatadir,
)

python = import('python')

conf = configuration_data()
conf.set('PYTHON', python.find_installation('python3').path())
conf.set('VERSION', meson.project_version())
conf.set('localedir', join_paths(get_option('prefix'), get_option('localedir')))
conf.set('pkgdatadir', pkgdatadir)

configure_file(
  input: 'regler.in',
  output: 'regler',
  configuration: conf,
  install: true,
  install_dir: get_option('bindir')
)

# zdep = dependency('libxdo3')



regler_sources = [
  '__init__.py',
  'firebase.json',
  'config.py',
  'main.py',
  'window.py',
  'Firebase.py',
  'App.py',
  'Actions.py'
]

# Include custom subdirs
install_data(regler_sources, install_dir: moduledir)
