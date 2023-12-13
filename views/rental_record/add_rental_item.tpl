<html>
<body>
<h2>Add Item</h2>
<hr/>
<form action="/add-rental" method="post">
  <p>First Name: <input name="fName"/></p>
  <p>Last Name: <input name="lName"/></p>
  <p>Movie Title: <input name="movie_title"/></p>
  <p>Movie Title: 
  <select name="movie_title">
    % for movie in movies_list:
        <option> {{movie['title']}}</option>
    % end
  </select>
  </p>
  <p>Date Borrow: <input name="date_borrow"/></p>
  <p>Due Date: <input name="due_date"/></p>
    <p><button type="submit">Submit</button></p>
</form>
<hr/>
</body>
</html>