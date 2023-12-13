<!DOCTYPE html>
<html>
<head>
    <title>Movies List</title>
    <script>
        function performSearch() {
            var searchTerm = document.getElementById("searchInput").value.toLowerCase();
            var allTitles = document.getElementsByClassName("movieTitle");

            for (var i = 0; i < allTitles.length; i++) {
                var currentTitle = allTitles[i].innerText.toLowerCase();
                var parentRow = allTitles[i].closest("tr");

                if (currentTitle.includes(searchTerm)) {
                    parentRow.style.display = "table-row";
                } else {
                    parentRow.style.display = "none";
                }
            }
        }
    </script>
</head>
<body>
    <h2>Movies List</h2>
    <form>
        <a href="/add-movie">Add new movie</a>
        <input type="text" id="searchInput" placeholder="Enter movie title" name="search result">
        <button type="button" onclick="performSearch()">Search</button>
    </form>
    <hr />
    <table>
        % for item in movies_list:
        <tr>
            <td>
                <p class="movieTitle">Title: {{item['title']}}</p>
                <p>Genre: {{item['genre']}}</p>
                <p>Year: {{item['year']}}</p>
                <p>Rated: {{item['rated']}}</p>
                <p>Runtime: {{item['runtime']}}</p>
                <div>
                    <a href="/update-movie/{{str(item['id'])}}">update</a>
                    <a href="/delete-movie/{{str(item['id'])}}">delete</a>
                </div>
            </td>
        </tr>
        % end
    </table>
    <hr />
</body>
</html>