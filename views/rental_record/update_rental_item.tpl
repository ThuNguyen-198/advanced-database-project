<!DOCTYPE html>
<html>
<body>
<h2>Update Record</h2>
<hr/>
<form action="/update-rental" method="post">
  <input type="hidden" name="id" value="{{id}}"/>

  <p >First Name: <input name="fName" value="{{fName}}"/></p>
  <p >Last Name: <input name="lName" value="{{lName}}"/></p>
  <p>Movie Title: 
  <select name="movie_title">
    <option> {{movie_title}}</option>
    % for movie in movies_list:
        <option> {{movie['title']}}</option>
    % end
  </select>
  </p>
  <p >Date Borrow: <input name="date_borrow" value="{{date_borrow}}"/></p>
  <p >Due Date: <input name="due_date" value="{{due_date}}"/></p>

  <p><button type="submit">Submit</button></p>
</form>
<hr/>
</body>
</html>