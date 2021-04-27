package playpants

import java.io.File

object TwirlGen {
  case class Params(sources: Seq[File] = Seq.empty,
                    sourceDir: File = new File("."),
                    templateImports: Seq[String] = Seq.empty,
                    target: File = new File("."))

  def main(args: Array[String]): Unit = {
    val parser = new scopt.OptionParser[Params]("twirl-gen") {
      head("twirl-gen", "1.0")
      opt[Seq[File]]("sources") valueName("<input1,input2>") action {
        (sources, c) => c.copy(sources = sources)
      } text("comma separated list of source files")

      opt[File]("source_dir") valueName("<source_dir>") action {
        (sourceDir, c) => c.copy(sourceDir = sourceDir)
      } text("Root directory for sources (to determine package name)")

      opt[Seq[String]]("template_imports") valueName("<import1,import2>") action {
        (templateImports, c) => c.copy(templateImports = templateImports)
      } text("Comma separated list of imports.")

      opt[File]("target") required() valueName("<target_dir>") action {
        (target, c) => c.copy(target = target)
      } text("directory to write generated sources")
    }

    parser.parse(args, Params()) match {
      case None => System.exit(1)
      case Some(params) =>
        params.sources.foreach {
          source =>
            val imports = params.templateImports.map {
              f => s"$f\n"
            }.mkString("import ")

            val r = play.twirl.compiler.TwirlCompiler.compile(
              source, params.sourceDir, params.target, "play.twirl.api.HtmlFormat",
              additionalImports=Seq(imports))
            println(s"HELLO: $source $r")
        }
    }
  }
}
