package playpants.tool

import java.io.File
import java.lang.reflect.Method
import java.{util => ju}

import play.core.{BuildDocHandler, BuildLink}
import playpants.tool.RunDev.Params

import scala.collection.JavaConverters._

class PantsBuildLink(params: Params) extends BuildLink {
  private var firstTime = true

  override def reload(): AnyRef = {
    if (firstTime) {
      firstTime = false
      getClass.getClassLoader
    } else null
  }

  override def projectPath(): File = params.projectPath

  override def settings(): ju.Map[String, String] = params.settings.asJava

  override def forceReload(): Unit = ???

  override def findSource(s: String, integer: Integer): Array[AnyRef] = {
    println(s"Find source: $s:$integer")
    Array.empty[AnyRef]
  }
}

object PantsDocHandler extends BuildDocHandler {
  override def maybeHandleDocRequest(request: scala.Any): AnyRef = None
}

object RunDev {
  case class Params(
    mainClass: String = "play.core.server.DevServerStart",
    projectPath: File = new File("."),
    port: Int = 9000,
    address: String = "127.0.0.1",
    settings: Map[String, String] = Map.empty)

  val parser = new scopt.OptionParser[Params]("play-dev") {
    head("play-dev", "1.0")
    opt[String]("mainClass") valueName("<mainClass>") action {
      (x, c) => c.copy(mainClass = x)
    } text("Main class")

    opt[File]("projectPath") required() valueName("<path>") action {
      (x, c) => c.copy(projectPath = x)
    } text("Path for root of project")

    opt[Map[String, String]]("settings") valueName("<key1=value1,key2=value2>") action {
      (x, c) => c.copy(settings = x)
    } text("Settings, comma separated key=value pairs")

    opt[String]("address") valueName("<address>") action {
      (x, c) => c.copy(address = x)
    } text("Address to bind")

    opt[Int]("port") valueName("<port>") action {
      (x, c) => c.copy(port = x)
    } text("Port to bind")
  }

  def main(args: Array[String]): Unit = {
    parser.parse(args, Params()) match {
      case None => System.exit(1)
      case Some(params) =>
        val mainClass = Class.forName(params.mainClass)
        val mainDev: Method = mainClass.getMethod("mainDevHttpMode", classOf[BuildLink], classOf[BuildDocHandler], classOf[Int], classOf[String])
        mainDev.invoke(null, new PantsBuildLink(params), PantsDocHandler, params.port: java.lang.Integer, params.address)
    }
  }
}
