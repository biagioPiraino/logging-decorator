# Logging Decorator
<h3> Description </h3>
<p> 
  Create a logging decorator (<em>@logit</em>) that stores logging information in a PostgreSQL table. 
  The <em>logging</em> table contains information about the method called, and the user who called the method.
</p>
<hr>

<h3>Prerequisites</h3>
Have an active <a href="https://www.postgresql.org/" target="_blank">PostgreSQL</a> server running locally.
<hr>

<h3>How to use</h3>

1) Create an .env file in the projects' root folder containing the following database-related variables:

<table>
  <tr>
    <td>HOST</td>
    <td>PORT</td>
    <td>DB_NAME</td>
    <td>USER</td>
    <td>PASSWORD</td>
  </tr>
</table>

2) Create a .venv folder in the projects' root folder, create a virtual environment by running the command <code>$ virtualenv .venv</code> and install the <a href="https://pypi.org/project/psycopg2/" target="_blank"><em>psycopg2</em></a> package.

3) Access to a local PostgreSQL server using <code>$psql -U postgres</code>.

4) Run the <em>database_script.sql</em> using <code>$\i path\database_script.sql</code> once connected to the local server.

5) Activate the virtual environment using <code>$ source .venv/bin/activate</code>.

6) Run the <em>main.py</em> script.

7) Deactivate the virtual environment using <code>deactivate</code>.

<hr>
<h3>References</h3>
<table>
<thead>
  <tr>
    <th>References</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td>
      <a href="https://book.pythontips.com/en/latest/virtual_environment.html" target="_blank">Python virtual environments</a>
    </td>
  </tr>
  <tr>
    <td>
      <a href="https://book.pythontips.com/en/latest/decorators.html" target="_blank">Python decorators</a>
    </td>
  </tr>
  <tr>
    <td>
      <a href="https://www.psycopg.org/docs/" target="_blank">Psycopg 2.9.5 documentation</a>
    </td>
  </tr>
 </tbody>
 </table>
