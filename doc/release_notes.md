<font size="7">XCOFDK RTE - Release Notes</font> <br>
<table>
  <tr>
    <th></th>
    <th></th>
    <th></th>
  </tr>
  <tr>
     <td>Version</td>
     <td>:</td>
     <td>1.0</td>
  </tr>
  <tr>
     <td>Date</td>
     <td>:</td>
     <td>21.08.2026</td>
  </tr>
  <tr>
     <td>&copy<c>Copyright</c></td>
     <td>:</td>
     <td>2023-2026 Farzad Safa (<a href>farzad.safa@xcofdk.com</a>)</td>
  </tr>
  <tr>
     <td> </td>
     <td></td>
     <td>All rights reserved.</td>
  </tr>
  <tr>
     <td> </td>
     <td> </td>
     <td> </td>
  </tr>
</table>

<br>


# Table of Contents
<!-- TOC depthFrom:1 depthTo:6 withLinks:1 updateOnSave:1 orderedList:0 -->
- [Table of Contents](#table-of-contents)
  - [Release Highlights](#release-highlights)
    - [Release Highlights v1.0](#release-highlights-v10)
  - [Release Notes](#release-notes)
    - [Release Notes v1.0 - 21.08.2026](#release-notes-v10---21082026)
<!-- /TOC -->

<br>


## Release Highlights

### Release Highlights v1.0

- Representing the backend of the framework of XCOFDK, provide both public API and implementation of framework's RTE.
- Improved robustness and stability.
- Improved shutdown sequence.
- Start the RTE if initiated by an authorized frontend package only, e.g. PyPI package <tt>xcofdk</tt>, which is also referred to <br> 
  as the default frontend package. 
- Always provide the default functional scope to the default frontend package <tt>xcofdk</tt> whose use is free of charge. 
- Drop support for subclassing (from former classes <tt>XTask</tt> and <tt>XMainTask</tt>).
- Drop support for Python versions 3.10 and older.
- Drop support for experimental free-threaded Python.
- Use Cython extensions of protected subpackages when building install wheel. 

[TOC](#table-of-contents)
______

<br>


## Release Notes

### Release Notes v1.0 - 21.08.2026

- XRTE-643 – Resolve findings related to both stability and shutdown sequence
- XRTE-642 – Refactoring of coordinated shutdown sequence
- XRTE-602 – Drop support for Python versions older than 3.11
- XRTE-597 – Drop support for experimental free-threading
- XRTE-589 – Introduce package <tt>xcofdkrte</tt> which provides both public API and implementation of framework's RTE.

[TOC](#table-of-contents)
______
