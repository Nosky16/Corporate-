<!-- BEGIN: login.html -->
<!DOCTYPE html>
<html>
<head>
  <title>Login - Energy Commission of Nigeria</title>
  <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
  <style>
    body { background-color: #f8f9fa; font-family: Arial, sans-serif; }
    .header { background-color: #008000; color: white; padding: 10px 0; text-align: center; }
    .header img { height: 50px; margin: 0 10px; }
    .container { max-width: 600px; margin-top: 20px; }
    .welcome-section { text-align: center; margin-bottom: 20px; }
    .welcome-section img { max-width: 100%; height: auto; }
  </style>
</head>
<body>
  <div class="header">
    <img src="{{ url_for('static', filename='images/ecn-logo.png') }}" alt="ECN Logo" class="ecn-logo">
    <img src="{{ url_for('static', filename='images/coat-of-arms.png') }}" alt="Nigerian Coat of Arms" class="coat-of-arms">
    <h1>Energy Commission of Nigeria</h1>
  </div>
  <div class="container">
    <div class="welcome-section">
      <h2>Welcome to Energy Commission of Nigeria</h2>
      <p>Please log in to access your account.</p>
      <img src="{{ url_for('static', filename='images/thermal-energy-generation.jpg') }}" alt="Thermal Energy Generation" class="img-fluid">
    </div>
    {% if error %}
      <p class="text-danger text-center">{{ error }}</p>
    {% endif %}
    <form method="POST" class="p-4 border rounded bg-white">
      <div class="mb-3">
        <label for="name" class="form-label">Name</label>
        <input type="text" name="name" class="form-control" required>
      </div>
      <button type="submit" class="btn btn-primary w-100">Login</button>
      <a href="/register" class="btn btn-secondary w-100 mt-2">Register</a>
    </form>
  </div>
</body>
</html>
<!-- END: login.html -->

<!-- BEGIN: register.html -->
<!DOCTYPE html>
<html>
<head>
  <title>Register - Energy Commission of Nigeria</title>
  <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
  <style>
    body { background-color: #f8f9fa; font-family: Arial, sans-serif; }
    .header { background-color: #008000; color: white; padding: 10px 0; text-align: center; }
    .header img { height: 50px; margin: 0 10px; }
    .container { max-width: 600px; margin-top: 20px; }
    .welcome-section { text-align: center; margin-bottom: 20px; }
    .welcome-section img { max-width: 100%; height: auto; }
  </style>
</head>
<body>
  <div class="header">
    <img src="{{ url_for('static', filename='images/ecn-logo.png') }}" alt="ECN Logo" class="ecn-logo">
    <img src="{{ url_for('static', filename='images/coat-of-arms.png') }}" alt="Nigerian Coat of Arms" class="coat-of-arms">
    <h1>Energy Commission of Nigeria</h1>
  </div>
  <div class="container">
    <div class="welcome-section">
      <h2>Welcome to Energy Commission of Nigeria</h2>
      <p>Register to access our services.</p>
      <img src="{{ url_for('static', filename='images/thermal-energy-generation.jpg') }}" alt="Thermal Energy Generation" class="img-fluid">
    </div>
    {% if error %}
      <p class="text-danger text-center">{{ error }}</p>
    {% endif %}
    <form method="POST" class="p-4 border rounded bg-white">
      <div class="mb-3">
        <label for="name" class="form-label">Name</label>
        <input type="text" name="name" class="form-control" required>
      </div>
      <div class="mb-3 form-check">
        <input type="checkbox" name="is_admin" class="form-check-input" id="is_admin">
        <label for="is_admin" class="form-check-label">Register as Admin</label>
      </div>
      <button type="submit" class="btn btn-primary w-100">Register</button>
      <a href="/login" class="btn btn-secondary w-100 mt-2">Back to Login</a>
    </form>
  </div>
</body>
</html>
<!-- END: register.html -->

<!-- BEGIN: dashboard.html -->
<!DOCTYPE html>
<html>
<head>
  <title>Dashboard - Energy Commission of Nigeria</title>
  <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
  <style>
    body { background-color: #f8f9fa; font-family: Arial, sans-serif; }
    .header { background-color: #008000; color: white; padding: 10px 0; text-align: center; }
    .header img { height: 50px; margin: 0 10px; }
    .container { max-width: 600px; margin-top: 20px; }
    .welcome-section { text-align: center; margin-bottom: 20px; }
    .welcome-section img { max-width: 100%; height: auto; }
  </style>
</head>
<body>
  <div class="header">
    <img src="{{ url_for('static', filename='images/ecn-logo.png') }}" alt="ECN Logo" class="ecn-logo">
    <img src="{{ url_for('static', filename='images/coat-of-arms.png') }}" alt="Nigerian Coat of Arms" class="coat-of-arms">
    <h1>Energy Commission of Nigeria</h1>
  </div>
  <div class="container">
    <div class="welcome-section">
      <h2>Welcome, {{ name }}!</h2>
      <p>Manage your account and services.</p>
      <img src="{{ url_for('static', filename='images/thermal-energy-generation.jpg') }}" alt="Thermal Energy Generation" class="img-fluid">
    </div>
    <div class="mt-3">
      <a href="/savings" class="btn btn-primary w-100 mb-2">View Savings</a>
      <a href="/loan" class="btn btn-primary w-100 mb-2">Apply for Loan</a>
      <a href="/repayments" class="btn btn-primary w-100 mb-2">View Repayments</a>
      {% if is_admin %}
        <a href="/admin" class="btn btn-warning w-100 mb-2">Admin Dashboard</a>
      {% endif %}
      <a href="/logout" class="btn btn-danger w-100">Logout</a>
    </div>
  </div>
</body>
</html>
<!-- END: dashboard.html -->

<!-- BEGIN: savings.html -->
<!DOCTYPE html>
<html>
<head>
  <title>Savings - Energy Commission of Nigeria</title>
  <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
  <style>
    body { background-color: #f8f9fa; font-family: Arial, sans-serif; }
    .header { background-color: #008000; color: white; padding: 10px 0; text-align: center; }
    .header img { height: 50px; margin: 0 10px; }
    .container { max-width: 800px; margin-top: 20px; }
    .welcome-section { text-align: center; margin-bottom: 20px; }
    .welcome-section img { max-width: 100%; height: auto; }
    table { background-color: white; }
  </style>
</head>
<body>
  <div class="header">
    <img src="{{ url_for('static', filename='images/ecn-logo.png') }}" alt="ECN Logo" class="ecn-logo">
    <img src="{{ url_for('static', filename='images/coat-of-arms.png') }}" alt="Nigerian Coat of Arms" class="coat-of-arms">
    <h1>Energy Commission of Nigeria</h1>
  </div>
  <div class="container">
    <div class="welcome-section">
      <h2>Your Savings</h2>
      <p>View your savings details.</p>
      <img src="{{ url_for('static', filename='images/thermal-energy-generation.jpg') }}" alt="Thermal Energy Generation" class="img-fluid">
    </div>
    <p class="text-center">Total Savings: ₦{{ total }}</p>
    {% if savings %}
      <table class="table table-bordered">
        <thead>
          <tr>
            <th>Date</th>
            <th>Amount (₦)</th>
          </tr>
        </thead>
        <tbody>
          {% for saving in savings %}
            <tr>
              <td>{{ saving[1] }}</td>
              <td>{{ saving[0] }}</td>
            </tr>
          {% endfor %}
        </tbody>
      </table>
    {% else %}
      <p class="text-muted text-center">No savings recorded.</p>
    {% endif %}
    <a href="/dashboard" class="btn btn-secondary w-100 mt-3">Back</a>
  </div>
</body>
</html>
<!-- END: savings.html -->

<!-- BEGIN: loan.html -->
<!DOCTYPE html>
<html>
<head>
  <title>Loan Application - Energy Commission of Nigeria</title>
  <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
  <style>
    body { background-color: #f8f9fa; font-family: Arial, sans-serif; }
    .header { background-color: #008000; color: white; padding: 10px 0; text-align: center; }
    .header img { height: 50px; margin: 0 10px; }
    .container { max-width: 800px; margin-top: 20px; }
    .welcome-section { text-align: center; margin-bottom: 20px; }
    .welcome-section img { max-width: 100%; height: auto; }
    table { background-color: white; }
  </style>
</head>
<body>
  <div class="header">
    <img src="{{ url_for('static', filename='images/ecn-logo.png') }}" alt="ECN Logo" class="ecn-logo">
    <img src="{{ url_for('static', filename='images/coat-of-arms.png') }}" alt="Nigerian Coat of Arms" class="coat-of-arms">
    <h1>Energy Commission of Nigeria</h1>
  </div>
  <div class="container">
    <div class="welcome-section">
      <h2>Apply for a Loan</h2>
      <p>Submit your loan application.</p>
      <img src="{{ url_for('static', filename='images/thermal-energy-generation.jpg') }}" alt="Thermal Energy Generation" class="img-fluid">
    </div>
    {% if error %}
      <p class="text-danger text-center">{{ error }}</p>
    {% endif %}
    <form method="POST" class="p-4 border rounded bg-white">
      <div class="mb-3">
        <label for="type_of_loan" class="form-label">Type of Loan</label>
        <input type="text" name="type_of_loan" class="form-control" required>
      </div>
      <div class="mb-3">
        <label for="amount" class="form-label">Amount (₦)</label>
        <input type="number" name="amount" class="form-control" required>
      </div>
      <div class="mb-3">
        <label for="duration" class="form-label">Duration (Months)</label>
        <input type="number" name="duration" class="form-control" required>
      </div>
      <div class="mb-3">
        <label for="ecn_staff_no" class="form-label">ECN Staff No</label>
        <input type="text" name="ecn_staff_no" class="form-control" required>
      </div>
      <div class="mb-3">
        <label for="ippis_no" class="form-label">IPPIS No</label>
        <input type="text" name="ippis_no" class="form-control" required>
      </div>
      <div class="mb-3">
        <label for="designation" class="form-label">Designation</label>
        <input type="text" name="designation" class="form-control" required>
      </div>
      <div class="mb-3">
        <label for="phone_no" class="form-label">Phone No</label>
        <input type="text" name="phone_no" class="form-control" required>
      </div>
      <div class="mb-3">
        <label for="bank_name" class="form-label">Bank Name</label>
        <input type="text" name="bank_name" class="form-control" required>
      </div>
      <div class="mb-3">
        <label for="account_no" class="form-label">Account No</label>
        <input type="text" name="account_no" class="form-control" required>
      </div>
      <div class="mb-3">
        <label for="previous_month_salary" class="form-label">Previous Month Salary (₦)</label>
        <input type="number" name="previous_month_salary" class="form-control" required>
      </div>
      <div class="mb-3">
        <label for="guarantor1_name" class="form-label">Guarantor 1 Name</label>
        <input type="text" name="guarantor1_name" class="form-control" required>
      </div>
      <div class="mb-3">
        <label for="guarantor1_staff_no" class="form-label">Guarantor 1 Staff No</label>
        <input type="text" name="guarantor1_staff_no" class="form-control" required>
      </div>
      <div class="mb-3">
        <label for="guarantor1_designation" class="form-label">Guarantor 1 Designation</label>
        <input type="text" name="guarantor1_designation" class="form-control" required>
      </div>
      <div class="mb-3">
        <label for="guarantor1_phone_no" class="form-label">Guarantor 1 Phone No</label>
        <input type="text" name="guarantor1_phone_no" class="form-control" required>
      </div>
      <div class="mb-3">
        <label for="guarantor2_name" class="form-label">Guarantor 2 Name</label>
        <input type="text" name="guarantor2_name" class="form-control" required>
      </div>
      <div class="mb-3">
        <label for="guarantor2_staff_no" class="form-label">Guarantor 2 Staff No</label>
        <input type="text" name="guarantor2_staff_no" class="form-control" required>
      </div>
      <div class="mb-3">
        <label for="guarantor2_designation" class="form-label">Guarantor 2 Designation</label>
        <input type="text" name="guarantor2_designation" class="form-control" required>
      </div>
      <div class="mb-3">
        <label for="guarantor2_phone_no" class="form-label">Guarantor 2 Phone No</label>
        <input type="text" name="guarantor2_phone_no" class="form-control" required>
      </div>
      <button type="submit" class="btn btn-primary w-100">Apply</button>
    </form>

    <h2 class="mt-5">Loan Repayment Schedule</h2>
    {% if loan_history %}
      <table class="table table-bordered">
        <thead>
          <tr>
            <th>Loan Type</th>
            <th>Amount (₦)</th>
            <th>Due Date</th>
            <th>Status</th>
          </tr>
        </thead>
        <tbody>
          {% for loan in loan_history %}
            <tr>
              <td>{{ loan.type_of_loan }}</td>
              <td>{{ loan.amount }}</td>
              <td>{{ loan.date }}</td>
              <td>{{ loan.status }}</td>
            </tr>
          {% endfor %}
        </tbody>
      </table>
    {% else %}
      <p class="text-muted text-center">No repayment schedule available.</p>
    {% endif %}
    <a href="/dashboard" class="btn btn-secondary w-100 mt-3">Back</a>
  </div>
</body>
</html>
<!-- END: loan.html -->

<!-- BEGIN: repayments.html -->
<!DOCTYPE html>
<html>
<head>
  <title>Repayments - Energy Commission of Nigeria</title>
  <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
  <style>
    body { background-color: #f8f9fa; font-family: Arial, sans-serif; }
    .header { background-color: #008000; color: white; padding: 10px 0; text-align: center; }
    .header img { height: 50px; margin: 0 10px; }
    .container { max-width: 800px; margin-top: 20px; }
    .welcome-section { text-align: center; margin-bottom: 20px; }
    .welcome-section img { max-width: 100%; height: auto; }
    table { background-color: white; }
  </style>
</head>
<body>
  <div class="header">
    <img src="{{ url_for('static', filename='images/ecn-logo.png') }}" alt="ECN Logo" class="ecn-logo">
    <img src="{{ url_for('static', filename='images/coat-of-arms.png') }}" alt="Nigerian Coat of Arms" class="coat-of-arms">
    <h1>Energy Commission of Nigeria</h1>
  </div>
  <div class="container">
    <div class="welcome-section">
      <h2>Your Repayments</h2>
      <p>View your repayment schedule.</p>
      <img src="{{ url_for('static', filename='images/thermal-energy-generation.jpg') }}" alt="Thermal Energy Generation" class="img-fluid">
    </div>
    {% if repayments %}
      <table class="table table-bordered">
        <thead>
          <tr>
            <th>Due Date</th>
            <th>Amount (₦)</th>
            <th>Status</th>
          </tr>
        </thead>
        <tbody>
          {% for repayment in repayments %}
            <tr>
              <td>{{ repayment[1] }}</td>
              <td>{{ repayment[2] }}</td>
              <td>
                {% if repayment[3] == 1 %}
                  Paid
                {% else %}
                  Unpaid
                {% endif %}
              </td>
            </tr>
          {% endfor %}
        </tbody>
      </table>
    {% else %}
      <p class="text-muted text-center">No repayments due.</p>
    {% endif %}
    <a href="/dashboard" class="btn btn-secondary w-100 mt-3">Back</a>
  </div>
</body>
</html>
<!-- END: repayments.html -->

<!-- BEGIN: admin.html -->
<!DOCTYPE html>
<html>
<head>
  <title>Admin Dashboard - Energy Commission of Nigeria</title>
  <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
  <style>
    body { background-color: #f8f9fa; font-family: Arial, sans-serif; }
    .header { background-color: #008000; color: white; padding: 10px 0; text-align: center; }
    .header img { height: 50px; margin: 0 10px; }
    .container { max-width: 600px; margin-top: 20px; }
    .welcome-section { text-align: center; margin-bottom: 20px; }
    .welcome-section img { max-width: 100%; height: auto; }
  </style>
</head>
<body>
  <div class="header">
    <img src="{{ url_for('static', filename='images/ecn-logo.png') }}" alt="ECN Logo" class="ecn-logo">
    <img src="{{ url_for('static', filename='images/coat-of-arms.png') }}" alt="Nigerian Coat of Arms" class="coat-of-arms">
    <h1>Energy Commission of Nigeria</h1>
  </div>
  <div class="container">
    <div class="welcome-section">
      <h2>Admin Dashboard</h2>
      <p>Manage staff and loan approvals.</p>
      <img src="{{ url_for('static', filename='images/thermal-energy-generation.jpg') }}" alt="Thermal Energy Generation" class="img-fluid">
    </div>
    <div class="mt-3">
      <a href="/add_savings" class="btn btn-primary w-100 mb-2">Add Savings</a>
      <a href="/users" class="btn btn-primary w-100 mb-2">View Users</a>
      <a href="/approve_loans" class="btn btn-primary w-100 mb-2">Approve Loans</a>
      <a href="/mark_staff_repayment" class="btn btn-primary w-100 mb-2">Mark Staff Repayment</a>
      <a href="/dashboard" class="btn btn-secondary w-100">Back to Dashboard</a>
    </div>
  </div>
</body>
</html>
<!-- END: admin.html -->

<!-- BEGIN: add_savings.html -->
<!DOCTYPE html>
<html>
<head>
  <title>Add Savings - Energy Commission of Nigeria</title>
  <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
  <style>
    body { background-color: #f8f9fa; font-family: Arial, sans-serif; }
    .header { background-color: #008000; color: white; padding: 10px 0; text-align: center; }
    .header img { height: 50px; margin: 0 10px; }
    .container { max-width: 600px; margin-top: 20px; }
    .welcome-section { text-align: center; margin-bottom: 20px; }
    .welcome-section img { max-width: 100%; height: auto; }
  </style>
</head>
<body>
  <div class="header">
    <img src="{{ url_for('static', filename='images/ecn-logo.png') }}" alt="ECN Logo" class="ecn-logo">
    <img src="{{ url_for('static', filename='images/coat-of-arms.png') }}" alt="Nigerian Coat of Arms" class="coat-of-arms">
    <h1>Energy Commission of Nigeria</h1>
  </div>
  <div class="container">
    <div class="welcome-section">
      <h2>Add Savings</h2>
      <p>Add savings for staff members.</p>
      <img src="{{ url_for('static', filename='images/thermal-energy-generation.jpg') }}" alt="Thermal Energy Generation" class="img-fluid">
    </div>
    {% if error %}
      <p class="text-danger text-center">{{ error }}</p>
    {% endif %}
    <form method="POST" class="p-4 border rounded bg-white">
      <div class="mb-3">
        <label for="staff_id" class="form-label">Staff ID</label>
        <select name="staff_id" class="form-control" required>
          <option value="">Select Staff</option>
          {% for user in users %}
            <option value="{{ user[0] }}">{{ user[0] }} - {{ user[1] }}</option>
          {% endfor %}
        </select>
      </div>
      <div class="mb-3">
        <label for="amount" class="form-label">Amount (₦)</label>
        <input type="number" name="amount" class="form-control" required>
      </div>
      <button type="submit" class="btn btn-primary w-100">Add Savings</button>
    </form>
    <a href="/admin" class="btn btn-secondary w-100 mt-3">Back</a>
  </div>
</body>
</html>
<!-- END: add_savings.html -->

<!-- BEGIN: users.html -->
<!DOCTYPE html>
<html>
<head>
  <title>Users - Energy Commission of Nigeria</title>
  <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
  <style>
    body { background-color: #f8f9fa; font-family: Arial, sans-serif; }
    .header { background-color: #008000; color: white; padding: 10px 0; text-align: center; }
    .header img { height: 50px; margin: 0 10px; }
    .container { max-width: 800px; margin-top: 20px; }
    .welcome-section { text-align: center; margin-bottom: 20px; }
    .welcome-section img { max-width: 100%; height: auto; }
    table { background-color: white; }
  </style>
</head>
<body>
  <div class="header">
    <img src="{{ url_for('static', filename='images/ecn-logo.png') }}" alt="ECN Logo" class="ecn-logo">
    <img src="{{ url_for('static', filename='images/coat-of-arms.png') }}" alt="Nigerian Coat of Arms" class="coat-of-arms">
    <h1>Energy Commission of Nigeria</h1>
  </div>
  <div class="container">
    <div class="welcome-section">
      <h2>Users</h2>
      <p>View all registered users.</p>
      <img src="{{ url_for('static', filename='images/thermal-energy-generation.jpg') }}" alt="Thermal Energy Generation" class="img-fluid">
    </div>
    {% if users %}
      <table class="table table-bordered">
        <thead>
          <tr>
            <th>ID</th>
            <th>Name</th>
          </tr>
        </thead>
        <tbody>
          {% for user in users %}
            <tr>
              <td>{{ user[0] }}</td>
              <td>{{ user[1] }}</td>
            </tr>
          {% endfor %}
        </tbody>
      </table>
    {% else %}
      <p class="text-muted text-center">No users found.</p>
    {% endif %}
    <a href="/admin" class="btn btn-secondary w-100 mt-3">Back</a>
  </div>
</body>
</html>
<!-- END: users.html -->

<!-- BEGIN: approve_loans.html -->
<!DOCTYPE html>
<html>
<head>
  <title>Approve Loans - Energy Commission of Nigeria</title>
  <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
  <style>
    body { background-color: #f8f9fa; font-family: Arial, sans-serif; }
    .header { background-color: #008000; color: white; padding: 10px 0; text-align: center; }
    .header img { height: 50px; margin: 0 10px; }
    .container { max-width: 1200px; margin-top: 20px; }
    .welcome-section { text-align: center; margin-bottom: 20px; }
    .welcome-section img { max-width: 100%; height: auto; }
    table { background-color: white; }
  </style>
</head>
<body>
  <div class="header">
    <img src="{{ url_for('static', filename='images/ecn-logo.png') }}" alt="ECN Logo" class="ecn-logo">
    <img src="{{ url_for('static', filename='images/coat-of-arms.png') }}" alt="Nigerian Coat of Arms" class="coat-of-arms">
    <h1>Energy Commission of Nigeria</h1>
  </div>
  <div class="container">
    <div class="welcome-section">
      <h2>Pending Loan Applications</h2>
      <p>Review and approve or reject loan applications.</p>
      <img src="{{ url_for('static', filename='images/thermal-energy-generation.jpg') }}" alt="Thermal Energy Generation" class="img-fluid">
    </div>
    {% if pending_applications %}
      <table class="table table-bordered">
        <thead>
          <tr>
            <th>User</th>
            <th>Amount (₦)</th>
            <th>Duration (Months)</th>
            <th>ECN Staff No</th>
            <th>IPPIS No</th>
            <th>Designation</th>
            <th>Phone No</th>
            <th>Bank Name</th>
            <th>Account No</th>
            <th>Prev. Month Salary (₦)</th>
            <th>Guarantor 1 Name</th>
            <th>Guarantor 1 Staff No</th>
            <th>Guarantor 1 Designation</th>
            <th>Guarantor 1 Phone No</th>
            <th>Guarantor 2 Name</th>
            <th>Guarantor 2 Staff No</th>
            <th>Guarantor 2 Designation</th>
            <th>Guarantor 2 Phone No</th>
            <th>Action</th>
          </tr>
        </thead>
        <tbody>
          {% for app in pending_applications %}
            <tr>
              <td>{{ app[11] }}</td>
              <td>{{ app[2] }}</td>
              <td>{{ app[3] }}</td>
              <td>{{ app[4] }}</td>
              <td>{{ app[5] }}</td>
              <td>{{ app[6] }}</td>
              <td>{{ app[7] }}</td>
              <td>{{ app[8] }}</td>
              <td>{{ app[9] }}</td>
              <td>{{ app[10] }}</td>
              <td>{{ app[12] }}</td>
              <td>{{ app[13] }}</td>
              <td>{{ app[14] }}</td>
              <td>{{ app[15] }}</td>
              <td>{{ app[16] }}</td>
              <td>{{ app[17] }}</td>
              <td>{{ app[18] }}</td>
              <td>{{ app[19] }}</td>
              <td>
                <a href="/approve/{{ app[0] }}" class="btn btn-sm btn-success">Approve</a>
                <a href="/reject/{{ app[0] }}" class="btn btn-sm btn-danger">Reject</a>
              </td>
            </tr>
          {% endfor %}
        </tbody>
      </table>
    {% else %}
      <p class="text-muted text-center">No pending loan applications.</p>
    {% endif %}

    <h2 class="mt-5">Approved Loans</h2>
    {% if approved_loans %}
      <table class="table table-bordered">
        <thead>
          <tr>
            <th>User</th>
            <th>Amount (₦)</th>
            <th>Duration (Months)</th>
            <th>ECN Staff No</th>
            <th>IPPIS No</th>
            <th>Designation</th>
            <th>Phone No</th>
            <th>Bank Name</th>
            <th>Account No</th>
            <th>Prev. Month Salary (₦)</th>
            <th>Action</th>
          </tr>
        </thead>
        <tbody>
          {% for loan in approved_loans %}
            <tr>
              <td>{{ loan[11] }}</td>
              <td>{{ loan[2] }}</td>
              <td>{{ loan[3] }}</td>
              <td>{{ loan[4] }}</td>
              <td>{{ loan[5] }}</td>
              <td>{{ loan[6] }}</td>
              <td>{{ loan[7] }}</td>
              <td>{{ loan[8] }}</td>
              <td>{{ loan[9] }}</td>
              <td>{{ loan[10] }}</td>
              <td>
                <a href="/loan_approval_details/{{ loan[0] }}" class="btn btn-sm btn-primary">Edit Details</a>
              </td>
            </tr>
          {% endfor %}
        </tbody>
      </table>
    {% else %}
      <p class="text-muted text-center">No approved loans.</p>
    {% endif %}
    <a href="/admin" class="btn btn-secondary w-100 mt-3">Back</a>
  </div>
</body>
</html>
<!-- END: approve_loans.html -->

<!-- BEGIN: loan_approval_details.html -->
<!DOCTYPE html>
<html>
<head>
  <title>Edit Loan Details - Energy Commission of Nigeria</title>
  <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
  <style>
    body { background-color: #f8f9fa; font-family: Arial, sans-serif; }
    .header { background-color: #008000; color: white; padding: 10px 0; text-align: center; }
    .header img { height: 50px; margin: 0 10px; }
    .container { max-width: 600px; margin-top: 20px; }
    .welcome-section { text-align: center; margin-bottom: 20px; }
    .welcome-section img { max-width: 100%; height: auto; }
  </style>
</head>
<body>
  <div class="header">
    <img src="{{ url_for('static', filename='images/ecn-logo.png') }}" alt="ECN Logo" class="ecn-logo">
    <img src="{{ url_for('static', filename='images/coat-of-arms.png') }}" alt="Nigerian Coat of Arms" class="coat-of-arms">
    <h1>Energy Commission of Nigeria</h1>
  </div>
  <div class="container">
    <div class="welcome-section">
      <h2>Edit Loan Details</h2>
      <p>Modify the details of the approved loan.</p>
      <img src="{{ url_for('static', filename='images/thermal-energy-generation.jpg') }}" alt="Thermal Energy Generation" class="img-fluid">
    </div>
    <p>Loan ID: {{ loan[0] }}</p>
    <p>User ID: {{ loan[1] }}</p>
    <p>Type of Loan: {{ loan[2] }}</p>
    <p>Requested Amount: ₦{{ loan[3] }}</p>
    <p>Duration: {{ loan[4] }} months</p>
    <form method="POST" class="p-4 border rounded bg-white">
      <div class="mb-3">
        <label for="amount_approved" class="form-label">Approved Amount (₦)</label>
        <input type="number" name="amount_approved" class="form-control" value="{{ loan[15] }}" required>
      </div>
      <div class="mb-3">
        <label for="interest_charged" class="form-label">Interest Charged (₦)</label>
        <input type="number" name="interest_charged" class="form-control" value="{{ loan[16] }}" required>
      </div>
      <div class="mb-3">
        <label for="total_amount" class="form-label">Total Amount to Repay (₦)</label>
        <input type="number" name="total_amount" class="form-control" value="{{ loan[17] }}" required>
      </div>
      <button type="submit" class="btn btn-primary w-100">Save Changes</button>
      <a href="/approve_loans" class="btn btn-secondary w-100 mt-2">Cancel</a>
    </form>
  </div>
</body>
</html>
<!-- END: loan_approval_details.html -->

<!-- BEGIN: mark_staff_repayment.html -->
<!DOCTYPE html>
<html>
<head>
  <title>Mark Staff Repayment - Energy Commission of Nigeria</title>
  <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
  <style>
    body { background-color: #f8f9fa; font-family: Arial, sans-serif; }
    .header { background-color: #008000; color: white; padding: 10px 0; text-align: center; }
    .header img { height: 50px; margin: 0 10px; }
    .container { max-width: 600px; margin-top: 20px; }
    .welcome-section { text-align: center; margin-bottom: 20px; }
    .welcome-section img { max-width: 100%; height: auto; }
  </style>
</head>
<body>
  <div class="header">
    <img src="{{ url_for('static', filename='images/ecn-logo.png') }}" alt="ECN Logo" class="ecn-logo">
    <img src="{{ url_for('static', filename='images/coat-of-arms.png') }}" alt="Nigerian Coat of Arms" class="coat-of-arms">
    <h1>Energy Commission of Nigeria</h1>
  </div>
  <div class="container">
    <div class="welcome-section">
      <h2>Mark Staff Repayment</h2>
      <p>Mark repayments as paid for staff members.</p>
      <img src="{{ url_for('static', filename='images/thermal-energy-generation.jpg') }}" alt="Thermal Energy Generation" class="img-fluid">
    </div>
    <form method="POST" class="p-4 border rounded bg-white">
      <div class="mb-3">
        <label for="staff_id" class="form-label">Select Staff</label>
        <select name="staff_id" class="form-control" required>
          <option value="">Select Staff</option>
          {% for user in users %}
            <option value="{{ user[0] }}">{{ user[1] }} (ID: {{ user[0] }})</option>
          {% endfor %}
        </select>
      </div>
      <div class="mb-3">
        <label for="repayment_id" class="form-label">Select Repayment</label>
        <select name="repayment_id" class="form-control" required>
          <option value="">Select Repayment</option>
          {% for user_id, repayments in repayments_data.items() %}
            {% for repayment in repayments %}
              <option value="{{ repayment[0] }}">Staff ID: {{ user_id }} - Due: {{ repayment[1] }} - Amount: ₦{{ repayment[2] }}</option>
            {% endfor %}
          {% endfor %}
        </select>
      </div>
      <button type="submit" class="btn btn-primary w-100">Mark as Paid</button>
    </form>
    <a href="/admin" class="btn btn-secondary w-100 mt-3">Back</a>
  </div>
</body>
</html>
<!-- END: mark_staff_repayment.html -->
