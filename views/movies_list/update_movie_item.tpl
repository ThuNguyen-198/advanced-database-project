<!DOCTYPE html>
<html>
<body>
<h2>Update Movie</h2>
<hr/>
<form action="/update-movie" method="post">
  <input type="hidden" name="id" value="{{id}}"/>

  <p >Title: <input name="title" value="{{title}}"/></p>
  <p >Genre: <input name="genre" value="{{genre}}"/></p>
  <p >Year: <input name="year" value="{{year}}"/></p>
  <p >Rated: <input name="rated" value="{{rated}}"/></p>
  <p >Runtime: <input name="runtime" value="{{runtime}}"/></p>

  <p><button type="submit">Submit</button></p>
</form>
<hr/>
</body>
</html>