java_library(
    name = 'play-pants-tool',
    sources = ['*.scala'],
    dependencies = [
        '3rdparty/jvm:twirl-compiler',
        '3rdparty/jvm:twirl-api',
        '3rdparty/jvm:twirl-parser',
        '3rdparty/jvm:routes-compiler',
        '3rdparty/jvm:scopt'],
    provides = artifact(org='com.thesamet', name='play-pants-tool', repo=public,
                        publication_metadata=publication_metadata('Runtime tool for play-pants.'))
    )

