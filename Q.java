// Decompiled by Jad v1.5.8e. Copyright 2001 Pavel Kouznetsov.
// Jad home page: http://www.geocities.com/kpdus/jad.html
// Decompiler options: packimports(3) 
// Source File Name:   Q.java


public final class Q
{

    Q()
    {
        t = x = y = z = 0.0D;
    }

    Q(float T)
    {
        t = T;
        x = y = z = 0.0D;
    }

    Q(float T, float X)
    {
        t = T;
        x = X;
        y = z = 0.0D;
    }

    Q(float T, float X, float Y)
    {
        t = T;
        x = X;
        y = Y;
        z = 0.0D;
    }

    Q(float T, float X, float Y, float Z)
    {
        t = T;
        x = X;
        y = Y;
        z = Z;
    }

    Q(Q q1)
    {
        t = q1.t;
        x = q1.x;
        y = q1.y;
        z = q1.z;
    }

    String qtoString()
    {
        StringBuffer s = new StringBuffer(t + "  ");
        if(x != 0.0D)
            s.append(x + " i  ");
        if(y != 0.0D)
            s.append(y + " j  ");
        if(z != 0.0D)
            s.append(z + " k  ");
        s.setLength(s.length() - 2);
        return s.toString();
    }

    String qtoString(int limit)
    {
        StringBuffer s = new StringBuffer();
        String stringN = new String();
        String sn = String.valueOf(t);
        if(sn.length() < limit)
        {
            s.append(sn + "  ");
        } else
        {
            int exp = sn.indexOf("E");
            exp = Math.max(exp, sn.indexOf("e"));
            if(exp < 0)
                s.append(sn.substring(0, limit) + "  ");
            else
            if(exp > limit)
                s.append(sn.substring(0, limit) + sn.substring(exp, sn.length()) + "  ");
            else
                s.append(sn + "  ");
        }
        if(x != 0.0D)
        {
            sn = String.valueOf(x);
            if(sn.length() < limit)
            {
                s.append(sn + " i  ");
            } else
            {
                int exp = sn.indexOf("E");
                if(exp < 0)
                    s.append(sn.substring(0, limit) + " i  ");
                else
                if(exp > limit)
                    s.append(sn.substring(0, limit) + sn.substring(exp, sn.length()) + " i  ");
                else
                    s.append(sn + " i  ");
            }
        }
        if(y != 0.0D)
        {
            sn = String.valueOf(y);
            if(sn.length() < limit)
            {
                s.append(sn + " j  ");
            } else
            {
                int exp = sn.indexOf("E");
                if(exp < 0)
                    s.append(sn.substring(0, limit) + " j  ");
                else
                if(exp > limit)
                    s.append(sn.substring(0, limit) + sn.substring(exp, sn.length()) + " i  ");
                else
                    s.append(sn + " j  ");
            }
        }
        if(z != 0.0D)
        {
            sn = String.valueOf(z);
            if(sn.length() < limit)
            {
                s.append(sn + " k  ");
            } else
            {
                int exp = sn.indexOf("E");
                if(exp < 0)
                    s.append(sn.substring(0, limit) + " k  ");
                else
                if(exp > limit)
                    s.append(sn.substring(0, limit) + sn.substring(exp, sn.length()) + " i  ");
                else
                    s.append(sn + " k  ");
            }
        }
        s.setLength(s.length() - 2);
        return s.toString();
    }

    public Q stringtoQ(String s)
    {
        int endt = s.indexOf("  ");
        int endx = s.indexOf(" i");
        int endy = s.indexOf(" j");
        int endz = s.indexOf(" k");
        Float t;
        if(endt == -1)
        {
            t = new Float(s.substring(0, s.length()));
            this.t = t.floatValue();
            this.x = this.y = this.z = 0.0D;
            return this;
        }
        t = new Float(s.substring(0, endt));
        this.t = t.floatValue();
        if(endx == -1)
        {
            this.x = 0.0D;
        } else
        {
            Float x = new Float(s.substring(endt + 2, endx));
            this.x = x.floatValue();
        }
        if(endy == -1)
        {
            this.y = 0.0D;
        } else
        {
            Float y = new Float(s.substring(Math.max(endt, endx) + 2, endy));
            this.y = y.floatValue();
        }
        if(endz == -1)
        {
            this.z = 0.0D;
        } else
        {
            Float z = new Float(s.substring(Math.max(Math.max(endt, endx), endy) + 2, endz));
            this.z = z.floatValue();
        }
        return this;
    }

    static Q qrandom(Q q1)
    {
        Q q = new Q();
        q.t = q1.t * Math.random();
        q.x = q1.x * Math.random();
        q.y = q1.y * Math.random();
        q.z = q1.z * Math.random();
        return q;
    }

    static Q qscalar(Q q1)
    {
        Q q = new Q();
        q.t = q1.t;
        return q;
    }

    static Q qvector(Q q1)
    {
        Q q = new Q();
        q.x = q1.x;
        q.y = q1.y;
        q.z = q1.z;
        return q;
    }

    static Q qconj(Q q1)
    {
        Q q = new Q();
        q.t = q1.t;
        q.x = -q1.x;
        q.y = -q1.y;
        q.z = -q1.z;
        return q;
    }

    static float norm(Q q1)
    {
        float n = q1.t * q1.t + q1.x * q1.x + q1.y * q1.y + q1.z * q1.z;
        return n;
    }

    static float sqrtNorm(Q q1)
    {
        float n = Math.sqrt(q1.t * q1.t + q1.x * q1.x + q1.y * q1.y + q1.z * q1.z);
        return n;
    }

    static float normVector(Q q1)
    {
        float n = q1.x * q1.x + q1.y * q1.y + q1.z * q1.z;
        return n;
    }

    static float sqrtNormVector(Q q1)
    {
        float n = Math.sqrt(q1.x * q1.x + q1.y * q1.y + q1.z * q1.z);
        return n;
    }

    static float det(Q q1)
    {
        float det = norm(q1);
        det *= det;
        return det;
    }

    static Q qsum(Q q1, Q q2)
    {
        Q q = new Q();
        q.t = q1.t + q2.t;
        q.x = q1.x + q2.x;
        q.y = q1.y + q2.y;
        q.z = q1.z + q2.z;
        return q;
    }

    static Q qdif(Q q1, Q q2)
    {
        Q q = new Q();
        q.t = q1.t - q2.t;
        q.x = q1.x - q2.x;
        q.y = q1.y - q2.y;
        q.z = q1.z - q2.z;
        return q;
    }

    static Q qinv(Q q1)
    {
        Q q = new Q();
        float n = 1.0D / norm(q1);
        q.t = q1.t * n;
        q.x = -q1.x * n;
        q.y = -q1.y * n;
        q.z = -q1.z * n;
        return q;
    }

    static Q qadj(Q q1)
    {
        Q q = new Q();
        float n = norm(q1);
        q.t = q1.t * n;
        q.x = -q1.x * n;
        q.y = -q1.y * n;
        q.z = -q1.z * n;
        return q;
    }

    static Q qxs(Q q1, float s)
    {
        Q q = new Q();
        q.t = q1.t * s;
        q.x = q1.x * s;
        q.y = q1.y * s;
        q.z = q1.z * s;
        return q;
    }

    static Q qx(Q q1, Q q2)
    {
        Q q = new Q();
        q.t = q1.t * q2.t - q1.x * q2.x - q1.y * q2.y - q1.z * q2.z;
        q.x = (q1.t * q2.x + q1.x * q2.t + q1.y * q2.z) - q1.z * q2.y;
        q.y = (q1.t * q2.y + q1.y * q2.t + q1.z * q2.x) - q1.x * q2.z;
        q.z = (q1.t * q2.z + q1.z * q2.t + q1.x * q2.y) - q1.y * q2.x;
        return q;
    }

    static Q qxeven(Q q1, Q q2)
    {
        Q q = new Q();
        q.t = q1.t * q2.t - q1.x * q2.x - q1.y * q2.y - q1.z * q2.z;
        q.x = q1.t * q2.x + q1.x * q2.t;
        q.y = q1.t * q2.y + q1.y * q2.t;
        q.z = q1.t * q2.z + q1.z * q2.t;
        return q;
    }

    static Q qxodd(Q q1, Q q2)
    {
        Q q = new Q();
        q.x = q1.y * q2.z - q1.z * q2.y;
        q.y = q1.z * q2.x - q1.x * q2.z;
        q.z = q1.x * q2.y - q1.y * q2.x;
        return q;
    }

    static Q qcx(Q q1, Q q2)
    {
        Q q = new Q();
        q.t = q1.t * q2.t + q1.x * q2.x + q1.y * q2.y + q1.z * q2.z;
        q.x = (q1.t * q2.x - q1.x * q2.t - q1.y * q2.z) + q1.z * q2.y;
        q.y = (q1.t * q2.y - q1.y * q2.t - q1.z * q2.x) + q1.x * q2.z;
        q.z = (q1.t * q2.z - q1.z * q2.t - q1.x * q2.y) + q1.y * q2.x;
        return q;
    }

    static Q qcxeven(Q q1, Q q2)
    {
        Q q = new Q();
        q.t = q1.t * q2.t + q1.x * q2.x + q1.y * q2.y + q1.z * q2.z;
        return q;
    }

    static Q qcxodd(Q q1, Q q2)
    {
        Q q = new Q();
        q.x = (q1.t * q2.x - q1.x * q2.t - q1.y * q2.z) + q1.z * q2.y;
        q.y = (q1.t * q2.y - q1.y * q2.t - q1.z * q2.x) + q1.x * q2.z;
        q.z = (q1.t * q2.z - q1.z * q2.t - q1.x * q2.y) + q1.y * q2.x;
        return q;
    }

    static float sinh(float r)
    {
        if(Math.abs(r) > 0.10000000000000001D)
            return (Math.exp(r) - Math.exp(-r)) / 2D;
        float s = 1.0D;
        for(int i = 19; i > 2; i -= 2)
            s = (s * r * r) / (float)(i * (i - 1)) + 1.0D;

        return s * r;
    }

    static float cosh(float r)
    {
        return (Math.exp(r) + Math.exp(-r)) / 2D;
    }

    static Q qsin(Q q1)
    {
        Q q = new Q();
        float vnorm = sqrtNormVector(q1);
        float vfactor = 0.0D;
        if(vnorm != 0.0D)
            vfactor = (Math.cos(q1.t) * sinh(vnorm)) / vnorm;
        q = qxs(q1, vfactor);
        q.t = Math.sin(q1.t) * cosh(vnorm);
        return q;
    }

    static Q qcos(Q q1)
    {
        Q q = new Q();
        float vnorm = sqrtNormVector(q1);
        float vfactor = 0.0D;
        if(vnorm != 0.0D)
            vfactor = (-1D * Math.sin(q1.t) * sinh(vnorm)) / vnorm;
        q = qxs(q1, vfactor);
        q.t = Math.cos(q1.t) * cosh(vnorm);
        return q;
    }

    static Q qtan(Q q1)
    {
        Q q = new Q();
        q = qx(qsin(q1), qinv(qcos(q1)));
        return q;
    }

    static Q qasin(Q q1)
    {
        Q qv = new Q(0.0D, 1.0D);
        float vnorm = sqrtNormVector(q1);
        if(vnorm != 0.0D)
            qv = qvector(qxs(q1, 1.0D / vnorm));
        return qx(qv, qasinh(qx(q1, qconj(qv))));
    }

    static Q qacos(Q q1)
    {
        Q qv = new Q(0.0D, 1.0D);
        float vnorm = sqrtNormVector(q1);
        if(vnorm != 0.0D)
            qv = qvector(qxs(q1, -1D / vnorm));
        return qx(qv, qacosh(q1));
    }

    static Q qatan(Q q1)
    {
        Q qtemp1 = new Q();
        Q qv = new Q(0.0D, 1.0D);
        float vnorm = sqrtNormVector(q1);
        if(vnorm != 0.0D)
            qv = qvector(qxs(q1, 1.0D / vnorm));
        return qx(qconj(qv), qatanh(qx(q1, qv)));
    }

    static Q qsinh(Q q1)
    {
        Q q = new Q();
        float vnorm = sqrtNormVector(q1);
        float vfactor = 0.0D;
        if(vnorm != 0.0D)
            vfactor = (cosh(q1.t) * Math.sin(vnorm)) / vnorm;
        q = qxs(q1, vfactor);
        q.t = sinh(q1.t) * Math.cos(vnorm);
        return q;
    }

    static Q qcosh(Q q1)
    {
        Q q = new Q();
        float vnorm = sqrtNormVector(q1);
        float vfactor = 0.0D;
        if(vnorm != 0.0D)
            vfactor = (sinh(q1.t) * Math.sin(vnorm)) / vnorm;
        q = qxs(q1, vfactor);
        q.t = cosh(q1.t) * Math.cos(vnorm);
        return q;
    }

    static Q qtanh(Q q1)
    {
        Q q = new Q();
        q = qx(qsinh(q1), qinv(qcosh(q1)));
        return q;
    }

    static Q qasinh(Q q1)
    {
        return qln(qsum(q1, qtotheN(qsum(qx(q1, q1), qone), 0.5D)));
    }

    static Q qacosh(Q q1)
    {
        Q qtemp1 = new Q();
        Q qtemp2 = new Q();
        qtemp1 = qsum(q1, qtotheN(qdif(qx(q1, q1), qone), 0.5D));
        qtemp2 = qdif(q1, qtotheN(qdif(qx(q1, q1), qone), 0.5D));
        if(norm(qtemp1) > norm(qtemp2))
            return qln(qtemp1);
        else
            return qxs(qln(qtemp2), -1D);
    }

    static Q qatanh(Q q1)
    {
        Q q = new Q();
        q = qxs(qln(qx(qsum(qone, q1), qinv(qdif(qone, q1)))), 0.5D);
        if(normVector(q1) == 0.0D && q1.t > 1.0D)
            q.x *= -1D;
        return q;
    }

    static Q qln(Q q1)
    {
        Q q = new Q();
        float vnorm = sqrtNormVector(q1);
        float vfactor = 1.0D;
        if(vnorm != 0.0D)
            vfactor = Math.atan2(vnorm, q1.t) / vnorm;
        else
        if(q1.t > 0.0D)
        {
            q.t = Math.log(q1.t);
            return q;
        }
        q = qxs(q1, vfactor);
        if(vnorm == 0.0D && q1.t < 0.0D)
            q.x = 3.1415926535897931D;
        q.t = Math.log(q1.t * q1.t + vnorm * vnorm) / 2D;
        return q;
    }

    static Q qlog(Q q1)
    {
        return qxs(qln(q1), 1.0D / Math.log(10D));
    }

    static Q qlg(Q q1)
    {
        return qxs(qln(q1), 1.0D / Math.log(10D));
    }

    static Q qexp(Q q1)
    {
        Q q = new Q();
        float vnorm = sqrtNormVector(q1);
        float vfactor = 0.0D;
        if(vnorm != 0.0D)
        {
            vfactor = (Math.exp(q1.t) * Math.sin(vnorm)) / vnorm;
        } else
        {
            q.t = Math.exp(q1.t);
            return q;
        }
        q = qxs(q1, vfactor);
        q.t = Math.exp(q1.t) * Math.cos(vnorm);
        return q;
    }

    static Q qtotheN(Q q1, float n)
    {
        Q q = new Q();
        if(normVector(q1) == 0.0D && q1.t > 0.0D)
        {
            q.t = Math.pow(q1.t, n);
            return q;
        } else
        {
            q = qexp(qxs(qln(q1), n));
            return q;
        }
    }

    static Q qtotheQ(Q q1, Q q2)
    {
        Q q = new Q();
        if(normVector(q1) == 0.0D && normVector(q2) == 0.0D)
        {
            q.t = Math.pow(q1.t, q2.t);
            return q;
        } else
        {
            q = qexp(qx(qln(q1), q2));
            return q;
        }
    }

    float t;
    float x;
    float y;
    float z;
    public static final Q qzero = new Q();
    public static final Q qone = new Q(1.0D);

}
