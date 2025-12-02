
G.PROJECTOR

Introduction

  G.Projector is a Java application that enablesen you to explore a large collection of global
  and regional map projections and optionally re-project an input GIF, JPEG or PNG map image.
  The input map image must use the equirectangular projection or the cylindrical equal-area,
  Robinson or Winkel Tripel projection. Some KMZ files may also be used for input. Lon-lat
  gridlines and continental outlines may be drawn on the map, and the resulting map images may
  be saved to disk in GIF, JPEG, PDF, PNG, PS or TIFF form.

  G.Projector requires that Java 11 (or later) Runtime Environment be installed on your
  computer. Please read the accompanying JAVA_11 README file for details.


Downloading

  The current version of G.Projector, along with other information about the application,
  may always be found at
  https://www.giss.nasa.gov/tools/gprojector/


Installing and running the G.Projector for Windows Package

  After unzipping the downloaded G.Projector archive, simply move the G.Projector folder to
  wherever you prefer to keep your applications programs on your PC.

  The uncompressed package for Windows should include the following items:

  - Double-clickable G.Projector.exe application launcher.
  - Java application G.Projector.jar and library *.jar files in a sub-directory called "jars".
  - Sample input map images in a sub-directory called "sample_maps".
  - This README file.

  To run G.Projector, just double-click on the G.Projector.exe application icon.


Trouble-Shooting

  You _must_ manually unzip the GProjector.zip archive file or else G.Projector will not work.
  Do not simply open the zip file on your desktop and doubleclick on the G.Projector.exe icon.

  The folder called "jars" _must_ remain in the same location as the G.Projector.exe launcher.
  Also, any .jar files in that folder must remain there. If you move or remove the jars folder
  or any of its contents, G.Projector will not work.

  The G.Projector.exe Java launcher requires that certain keys/values regarding the Java installation
  have been set in the Windows Registry. However, some alternative Java distributions may not set
  these keys or else may require that you specifically enable them during installation. For
  example, if using the Adoptium Temurin installer, you must enable the options for "Set JAVA_HOME
  variable" and "JavaSoft (Oracle) registry keys" in the Custom Setup panel.


Continent Overlays Files

  If you are looking for additional overlay files compatible with G.Projector, any of the
  optional "outline overlays" available from the Panoply software website may be used. See
  https://www.giss.nasa.gov/tools/panoply/overlays/

  G.Projector can also use many outline or multipoint SHP shapefiles as overlays.

  To add an overlay to G.Projector's library, go to its Preferences window, select the
  Overlays tab, and click the "+" icon at lower left of the table listing of overlays.


Help and Other Documentation

  More details about using G.Projector are available at:
  https://www.giss.nasa.gov/tools/gprojector/help/


Contact

  Please send bug reports, etc., to the developer

  Robert B. Schmunk
  robert.b.schmunk@nasa.gov
  NASA Goddard Institute for Space Studies
  2880 Broadway, New York, NY 10025 USA


Acknowledgments

  G.Projector uses some Java classes and libraries written by third-party developers. A list,
  with hyperlinks to pertinent websites containing license information and source code, may be
  found in G.Projector's help windows or on the G.Projector website.

