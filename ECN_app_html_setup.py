<!-- BEGIN: login.html -->
<!DOCTYPE html>
<html>
<head>
  <!-- Page title for the login page -->
  <title>Login</title>
  <!-- Bootstrap CSS for styling -->
  <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
</head>
<body>
  <div class="container mt-4">
    <!-- Page heading -->
    <h2>Login</h2>
    <!-- Display error message if login fails -->
    {% if error %}
      <p class="text-danger">{{ error }}</p>
    {% endif %}
    <!-- Login form -->
    <form method="POST">
      <div class="mb-3">
        <label for="name" class="form-label">Name</label>
        <input type="text" name="name" class="form-control" required>
      </div>
      <button type="submit" class="btn btn-primary">Login</button>
      <!-- Link to the registration page -->
      <a href="/register" class="btn btn-secondary ms-2">Register</a>
    </form>
  </div>
</body>
</html>
<!-- END: login.html -->

<!-- BEGIN: register.html -->
<!DOCTYPE html>
<html>
<head>
  <!-- Page title for the registration page -->
  <title>Register</title>
  <!-- Bootstrap CSS for styling -->
  <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
</head>
<body>
  <div class="container mt-4">
    <!-- Page heading -->
    <h2>Register</h2>
    <!-- Display error message if registration fails -->
    {% if error %}
      <p class="text-danger">{{ error }}</p>
    {% endif %}
    <!-- Registration form -->
    <form method="POST">
      <div class="mb-3">
        <label for="name" class="form-label">Name</label>
        <input type="text" name="name" class="form-control" required>
      </div>
      <div class="mb-3 form-check">
        <input type="checkbox" name="is_admin" class="form-check-input" id="is_admin">
        <label for="is_admin" class="form-check-label">Register as Admin</label>
      </div>
      <button type="submit" class="btn btn-primary">Register</button>
      <!-- Link to the login page -->
      <a href="/login" class="btn btn-secondary ms-2">Back to Login</a>
    </form>
  </div>
</body>
</html>
<!-- END: register.html -->

<!-- BEGIN: dashboard.html -->
<!DOCTYPE html>
<html>
<head>
  <!-- Page title for the dashboard -->
  <title>Dashboard</title>
  <!-- Bootstrap CSS for styling -->
  <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
</head>
<body>
  <div class="container mt-4">
    <!-- Welcome message with the user's name -->
    <h2>Welcome, {{ name }}!</h2>
    <!-- Navigation links for all users -->
    <div class="mt-3">
      <a href="/savings" class="btn btn-primary">View Savings</a>
      <a href="/loan" class="btn btn-primary">Apply for Loan</a>
      <a href="/repayments" class="btn btn-primary">View Repayments</a>
      <!-- Additional links for admins -->
      {% if is_admin %}
        <a href="/admin" class="btn btn-warning">Admin Dashboard</a>
      {% endif %}
      <a href="/logout" class="btn btn-danger">Logout</a>
    </div>
  </div>
</body>
</html>
<!-- END: dashboard.html -->

<!-- BEGIN: savings.html -->
<!DOCTYPE html>
<html>
<head>
  <!-- Page title for the savings page -->
  <title>Savings</title>
  <!-- Bootstrap CSS for styling -->
  <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
</head>
<body>
  <div class="container mt-4">
    <!-- Page heading -->
    <h2>Your Savings</h2>
    <!-- Display total savings -->
    <p>Total Savings: ₦{{ total }}</p>
    <!-- Display savings history table -->
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
              <td>{{ saving[1] }}</td> <!-- Date -->
              <td>{{ saving[0] }}</td> <!-- Amount -->
            </tr>
          {% endfor %}
        </tbody>
      </table>
    {% else %}
      <!-- Message if no savings are available -->
      <p class="text-muted">No savings recorded.</p>
    {% endif %}
    <!-- Back to dashboard link -->
    <a href="/dashboard" class="btn btn-secondary mt-3">Back</a>
  </div>
</body>
</html>
<!-- END: savings.html -->

<!-- BEGIN: loan.html -->
<!DOCTYPE html>
<html>
<head>
  <!-- Page title for the loan application page -->
  <title>Loan Application</title>
  <!-- Bootstrap CSS for styling -->
  <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
</head>
<body>
  <div class="container mt-4">
    <!-- Section for loan application form -->
    <h2>Apply for a Loan</h2>
    <!-- Display error message if form submission fails -->
    {% if error %}
      <p class="text-danger">{{ error }}</p>
    {% endif %}
    <!-- Loan application form -->
    <form method="POST">
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
      <button type="submit" class="btn btn-primary">Apply</button>
    </form>

    <!-- Section for displaying loan history -->
    <h2 class="mt-5">Loan History</h2>
    {% if loan_history %}
      <table class="table table-bordered">
        <thead>
          <tr>
            <th>Loan Type</th>
            <th>Amount (₦)</th>
            <th>Duration (Months)</th>
            <th>Date Applied</th>
            <th>Status</th>
            <th>Amount Owing (₦)</th>
          </tr>
        </thead>
        <tbody>
          {% for loan in loan_history %}
            <tr>
              <td>{{ loan.type_of_loan }}</td>
              <td>{{ loan.amount }}</td>
              <td>{{ loan.duration }}</td>
              <td>{{ loan.date }}</td>
              <td>{{ loan.status | capitalize }}</td>
              <td>
                {% if loan.amount_owing is not none %}
                  {{ loan.amount_owing }}
                {% else %}
                  N/A
                {% endif %}
              </td>
            </tr>
          {% endfor %}
        </tbody>
      </table>
    {% else %}
      <!-- Message if no loan history is available -->
      <p class="text-muted">No loan history available.</p>
    {% endif %}
    <!-- Back to dashboard link -->
    <a href="/dashboard" class="btn btn-secondary mt-3">Back</a>
  </div>
</body>
</html>
<!-- END: loan.html -->

<!-- BEGIN: repayments.html -->
<!DOCTYPE html>
<html>
<head>
  <!-- Page title for the repayments page -->
  <title>Repayments</title>
  <!-- Bootstrap CSS for styling -->
  <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
</head>
<body>
  <div class="container mt-4">
    <!-- Page heading -->
    <h2>Your Repayments</h2>
    <!-- Display repayments table -->
    {% if repayments %}
      <table class="table table-bordered">
        <thead>
          <tr>
            <th>Due Date</th>
            <th>Amount (₦)</th>
            <th>Status</th>
            <th>Action</th>
          </tr>
        </thead>
        <tbody>
          {% for repayment in repayments %}
            <tr>
              <td>{{ repayment[1] }}</td> <!-- Due Date -->
              <td>{{ repayment[2] }}</td> <!-- Amount -->
              <td>
                {% if repayment[3] == 1 %}
                  Paid
                {% else %}
                  Unpaid
                {% endif %}
              </td>
              <td>
                {% if repayment[3] == 0 %}
                  <a href="/mark_paid/{{ repayment[0] }}" class="btn btn-sm btn-success">Mark as Paid</a>
                {% else %}
                  N/A
                {% endif %}
              </td>
            </tr>
          {% endfor %}
        </tbody>
      </table>
    {% else %}
      <!-- Message if no repayments are available -->
      <p class="text-muted">No repayments due.</p>
    {% endif %}
    <!-- Back to dashboard link -->
    <a href="/dashboard" class="btn btn-secondary mt-3">Back</a>
  </div>
</body>
</html>
<!-- END: repayments.html -->

<!-- BEGIN: admin.html -->
<!DOCTYPE html>
<html>
<head>
  <!-- Page title for the admin dashboard -->
  <title>Admin Dashboard</title>
  <!-- Bootstrap CSS for styling -->
  <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
</head>
<body>
  <div class="container mt-4">
    <!-- Page heading -->
    <h2>Admin Dashboard</h2>
    <!-- Navigation links for admin functionalities -->
    <div class="mt-3">
      <a href="/add_savings" class="btn btn-primary">Add Savings</a>
      <a href="/users" class="btn btn-primary">View Users</a>
      <a href="/approve_loans" class="btn btn-primary">Approve Loans</a>
      <a href="/dashboard" class="btn btn-secondary">Back to Dashboard</a>
    </div>
  </div>
</body>
</html>
<!-- END: admin.html -->

<!-- BEGIN: add_savings.html -->
<!DOCTYPE html>
<html>
<head>
  <!-- Page title for the add savings page -->
  <title>Add Savings</title>
  <!-- Bootstrap CSS for styling -->
  <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
</head>
<body>
  <div class="container mt-4">
    <!-- Page heading -->
    <h2>Add Savings</h2>
    <!-- Display error message if form submission fails -->
    {% if error %}
      <p class="text-danger">{{ error }}</p>
    {% endif %}
    <!-- Form to add savings -->
    <form method="POST">
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
      <button type="submit" class="btn btn-primary">Add Savings</button>
    </form>
    <!-- Back to admin dashboard link -->
    <a href="/admin" class="btn btn-secondary mt-3">Back</a>
  </div>
</body>
</html>
<!-- END: add_savings.html -->

<!-- BEGIN: users.html -->
<!DOCTYPE html>
<html>
<head>
  <!-- Page title for the users page -->
  <title>Users</title>
  <!-- Bootstrap CSS for styling -->
  <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
</head>
<body>
  <div class="container mt-4">
    <!-- Page heading -->
    <h2>Users</h2>
    <!-- Display users table -->
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
              <td>{{ user[0] }}</td> <!-- User ID -->
              <td>{{ user[1] }}</td> <!-- User Name -->
            </tr>
          {% endfor %}
        </tbody>
      </table>
    {% else %}
      <!-- Message if no users are available -->
      <p class="text-muted">No users found.</p>
    {% endif %}
    <!-- Back to admin dashboard link -->
    <a href="/admin" class="btn btn-secondary mt-3">Back</a>
  </div>
</body>
</html>
<!-- END: users.html -->

<!-- BEGIN: approve_loans.html -->
<!DOCTYPE html>
<html>
<head>
  <!-- Page title for the approve loans page -->
  <title>Approve Loans</title>
  <!-- Bootstrap CSS for styling -->
  <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
</head>
<body>
  <div class="container mt-4">
    <!-- Section for pending loan applications -->
    <h2>Pending Loan Applications</h2>
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
              <td>{{ app[11] }}</td> <!-- u.name -->
              <td>{{ app[2] }}</td> <!-- l.amount -->
              <td>{{ app[3] }}</td> <!-- l.duration -->
              <td>{{ app[4] }}</td> <!-- l.ecn_staff_no -->
              <td>{{ app[5] }}</td> <!-- l.ippis_no -->
              <td>{{ app[6] }}</td> <!-- l.designation -->
              <td>{{ app[7] }}</td> <!-- l.phone_no -->
              <td>{{ app[8] }}</td> <!-- l.bank_name -->
              <td>{{ app[9] }}</td> <!-- l.account_no -->
              <td>{{ app[10] }}</td> <!-- l.previous_month_salary -->
              <td>{{ app[12] }}</td> <!-- l.guarantor1_name -->
              <td>{{ app[13] }}</td> <!-- l.guarantor1_staff_no -->
              <td>{{ app[14] }}</td> <!-- l.guarantor1_designation -->
              <td>{{ app[15] }}</td> <!-- l.guarantor1_phone_no -->
              <td>{{ app[16] }}</td> <!-- l.guarantor2_name -->
              <td>{{ app[17] }}</td> <!-- l.guarantor2_staff_no -->
              <td>{{ app[18] }}</td> <!-- l.guarantor2_designation -->
              <td>{{ app[19] }}</td> <!-- l.guarantor2_phone_no -->
              <td>
                <!-- Approve and reject buttons -->
                <a href="/approve/{{ app[0] }}" class="btn btn-sm btn-success">Approve</a>
                <a href="/reject/{{ app[0] }}" class="btn btn-sm btn-danger">Reject</a>
              </td>
            </tr>
          {% endfor %}
        </tbody>
      </table>
    {% else %}
      <!-- Message if no pending applications -->
      <p class="text-muted">No pending loan applications.</p>
    {% endif %}

    <!-- Section for approved loans -->
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
              <td>{{ loan[11] }}</td> <!-- u.name -->
              <td>{{ loan[2] }}</td> <!-- l.amount -->
              <td>{{ loan[3] }}</td> <!-- l.duration -->
              <td>{{ loan[4] }}</td> <!-- l.ecn_staff_no -->
              <td>{{ loan[5] }}</td> <!-- l.ippis_no -->
              <td>{{ loan[6] }}</td> <!-- l.designation -->
              <td>{{ loan[7] }}</td> <!-- l.phone_no -->
              <td>{{ loan[8] }}</td> <!-- l.bank_name -->
              <td>{{ loan[9] }}</td> <!-- l.account_no -->
              <td>{{ loan[10] }}</td> <!-- l.previous_month_salary -->
              <td>
                <!-- Edit details button -->
                <a href="/loan_approval_details/{{ loan[0] }}" class="btn btn-sm btn-primary">Edit Details</a>
              </td>
            </tr>
          {% endfor %}
        </tbody>
      </table>
    {% else %}
      <!-- Message if no approved loans -->
      <p class="text-muted">No approved loans.</p>
    {% endif %}
    <!-- Back to admin dashboard link -->
    <a href="/admin" class="btn btn-secondary mt-3">Back</a>
  </div>
</body>
</html>
<!-- END: approve_loans.html -->


<!-- BEGIN: loan_approval_details.html -->
<!DOCTYPE html>
<html>
<head>
  <!-- Page title for the loan details editing page -->
  <title>Edit Loan Details</title>
  <!-- Bootstrap CSS for styling -->
  <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
</head>
<body>
  <div class="container mt-4">
    <!-- Page heading -->
    <h2>Edit Loan Details</h2>
    <!-- Display loan details -->
    <p>Loan ID: {{ loan[0] }}</p>
    <p>User ID: {{ loan[1] }}</p>
    <p>Type of Loan: {{ loan[2] }}</p>
    <p>Requested Amount: ₦{{ loan[3] }}</p>
    <p>Duration: {{ loan[4] }} months</p>
    <!-- Form to edit loan details -->
    <form method="POST">
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
      <button type="submit" class="btn btn-primary">Save Changes</button>
      <a href="/approve_loans" class="btn btn-secondary">Cancel</a>
    </form>
  </div>
</body>
</html>
<!-- END: loan_approval_details.html -->
