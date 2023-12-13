<html>
<body>
<h2>Movie Rental Record</h2>
<hr/>
<table>
% for item in rental_list:
  <tr>
    <td>
    <p>First Name: {{item['fName']}}</p>
    <p>Last Name: {{item['lName']}}</p>
    <p>Movie Title: {{item['movie_title']}}</p>
    <p>Date Borrow: {{item['date_borrow']}}</p>
    <p>Due Date: {{item['due_date']}}</p>
    <div>
    <a href="/update-rental/{{str(item['id'])}}">update</a> 
    <a href="/delete-rental/{{str(item['id'])}}">delete</a> 
    </div>
    </td>
  </tr>

% end
</table>
<hr/>
<a href="/add-rental">Add new record</a>
</body>
</html>