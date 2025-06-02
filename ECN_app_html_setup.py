<!-- ========== templates/login.html ========== -->
<!DOCTYPE html>
<html>
<head><title>Login</title></head>
<body>
  <h2>Login</h2>
  <form method="POST">
    <input type="text" name="name" placeholder="Enter your name" required>
    <button type="submit">Login</button>
  </form>
  <p>Don't have an account? <a href="/register">Register here</a></p>
</body>
</html>

<!-- ========== templates/register.html ========== -->
<!DOCTYPE html>
<html>
<head><title>Register</title></head>
<body>
  <h2>Register</h2>
  <form method="POST">
    <input type="text" name="name" placeholder="Enter your name" required>
    <label><input type="checkbox" name="is_admin"> Is Admin?</label><br><br>
    <button type="submit">Register</button>
  </form>
  <p>Already registered? <a href="/login">Login here</a></p>
</body>
</html>

<!-- ========== templates/dashboard.html ========== -->
<!DOCTYPE html>
<html>
<head><title>Dashboard</title></head>
<body>
  <h2>Welcome, {{ name }}</h2>
  <ul>
    <li><a href="/savings">View Savings</a></li>
    <li><a href="/loan">Loan History / Request</a></li>
    <li><a href="/repayments">Repayment History</a></li>
    {% if is_admin %}
    <li><a href="/admin">Admin Dashboard</a></li>
    {% endif %}
    <li><a href="/logout">Logout</a></li>
  </ul>
</body>
</html>

<!-- ========== templates/savings.html ========== -->
<!DOCTYPE html>
<html>
<head><title>Savings</title></head>
<body>
  <h2>Total Savings: ₦{{ total }}</h2>
  <table border="1">
    <tr><th>Date</th><th>Amount</th></tr>
    {% for amount, date in savings %}
      <tr><td>{{ date }}</td><td>₦{{ amount }}</td></tr>
    {% endfor %}
  </table>
  <a href="/dashboard">Back</a>
</body>
</html>

<!-- ========== templates/loan.html ========== -->
<!DOCTYPE html>
<html>
<head><title>Loan</title></head>
<body>
  <h2>Loan History</h2>
  <table border="1">
    <tr><th>Amount</th><th>Duration (months)</th><th>Status</th><th>Date</th></tr>
    {% for loan in loans %}
      <tr><td>₦{{ loan[2] }}</td><td>{{ loan[3] }}</td><td>{{ loan[6] }}</td><td>{{ loan[5] }}</td></tr>
    {% endfor %}
  </table>
  <h3>Apply for a Loan</h3>
  <form method="POST">
    <input type="number" name="amount" placeholder="Loan Amount" required>
    <input type="number" name="duration" placeholder="Repayment Duration (months)" required>
    <button type="submit">Submit</button>
  </form>
  <a href="/dashboard">Back</a>
</body>
</html>

<!-- templates/repayments.html -->
<!DOCTYPE html>
<html>
<head>
  <title>Repayments</title>
  <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
</head>
<body>
  <div class="container mt-4">
    <h2>Repayment Schedule</h2>
    {% if repayments %}
      <table class="table table-bordered">
        <thead>
          <tr>
            <th>Due Date</th>
            <th>Amount</th>
            <th>Status</th>
            <th>Action</th>
          </tr>
        </thead>
        <tbody>
          {% for repayment_id, due, amount, status in repayments %}
            <tr>
              <td>{{ due }}</td>
              <td>₦{{ amount }}</td>
              <td>{{ 'Unpaid' if status == 0 else 'Paid' }}</td>
              <td>
                {% if status == 0 %}
                  <a href="/mark_paid/{{ repayment_id }}" class="btn btn-sm btn-primary">Mark as Paid</a>
                {% endif %}
              </td>
            </tr>
          {% endfor %}
        </tbody>
      </table>
    {% else %}
      <p class="text-muted">No repayment schedule available.</p>
    {% endif %}
    <a href="/dashboard" class="btn btn-secondary mt-3">Back</a>
  </div>
</body>
</html>

<!-- ========== templates/admin.html ========== -->
<!DOCTYPE html>
<html>
<head><title>Admin Dashboard</title></head>
<body>
  <h2>Admin Controls</h2>
  <ul>
    <li><a href="/add_savings">Add Staff Savings</a></li>
    <li><a href="/users">View Staff</a></li>
    <li><a href="/approve_loans">Approve Loans</a></li>
    <li><a href="/dashboard">Back</a></li>
  </ul>
</body>
</html>

<!-- ========== templates/add_savings.html ========== -->
<!DOCTYPE html>
<html>
<head><title>Add Savings</title></head>
<body>
  <h2>Add Staff Savings</h2>
  <form method="POST">
    <input type="number" name="staff_id" placeholder="Staff ID" required>
    <input type="number" name="amount" placeholder="Amount" required>
    <button type="submit">Add</button>
  </form>
  <a href="/admin">Back</a>
</body>
</html>

<!-- ========== templates/users.html ========== -->
<!DOCTYPE html>
<html>
<head><title>Users</title></head>
<body>
  <h2>All Staff</h2>
  <table border="1">
    <tr><th>ID</th><th>Name</th></tr>
    {% for user in users %}
      <tr><td>{{ user[0] }}</td><td>{{ user[1] }}</td></tr>
    {% endfor %}
  </table>
  <a href="/admin">Back</a>
</body>
</html>

<!-- ========== templates/approve_loans.html ========== -->
<!DOCTYPE html>
<html>
<head><title>Approve Loans</title></head>
<body>
  <h2>Loan Requests</h2>
  <table border="1">
    <tr><th>Loan ID</th><th>Staff ID</th><th>Amount</th><th>Action</th></tr>
    {% for loan in loans %}
      <tr>
        <td>{{ loan[0] }}</td><td>{{ loan[1] }}</td><td>₦{{ loan[2] }}</td>
        <td><a href="/approve/{{ loan[0] }}">Approve</a></td>
      </tr>
    {% endfor %}
  </table>
  <a href="/admin">Back</a>
</body>
</html>
