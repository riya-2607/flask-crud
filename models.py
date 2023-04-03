class Student:
  def __init__(self, id, fname, lname, dob, amt_due):
    self.id = id
    self.fname = fname
    self.lname = lname
    self.dob = dob
    self.amt_due = amt_due

  def __repr__(self):
    return '<id {}>'.format(self.id)

  def serialize(self):
    return {
      'id': self.id,
      'fname': self.fname,
      'lname': self.lname,
      'dob':self.dob,
      'amt_due':self.amt_due
    }
