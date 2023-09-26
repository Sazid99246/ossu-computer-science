class A
  def m1
    34
  end

  def m2 (x, y)
    z = 7
    if x > y
      false
    else
        x + y * z
    end
    z += 3
  end
end


class B
  def m1
    4
  end

  def m3 x
    x.abs * 2 + self.m1
  end
end

class C
  def m1
    print "hi "
    self   
  end

  def m2
    print "bye "
    self
  end

  def m3
    print "\n"
    self
  end
end
