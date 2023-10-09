import java.util.Comparator;

class StudentComparatorAsc implements Comparator<Student> {
    public int compare(Student stu1, Student stu2) {
        double avgGrade = stu1.avgGrade() - stu2.avgGrade();

        if (avgGrade > 0)
            return 1;
        if (avgGrade < 0)
            return -1;
        return 0;
    }
}
