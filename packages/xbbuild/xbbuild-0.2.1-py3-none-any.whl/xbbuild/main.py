from xbutils.cmd import Cmd

Cmd.default_function_module = 'xbbuild'

Cmd(name='info', function=".info.info_cmd")
Cmd(name='zip-doc', function=".zip_doc.zip_doc_cmd",help='create a zip file from sphinx documentation')
Cmd(name='sphinx', function=".sphinx.sphinx_cmd",help='create documentation with sphinx')
Cmd(name='build-doc', function=".build_doc.build_doc_cmd",help ='sphinx + zip-doc')


def main():
    Cmd.main()


if __name__ == '__main__':
    main()
