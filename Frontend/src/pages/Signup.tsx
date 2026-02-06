import { useState } from 'react';
import { useNavigate, Link } from 'react-router-dom';
import { Button } from '@/components/ui/button';
import { Input } from '@/components/ui/input';
import { Label } from '@/components/ui/label';
import { Card, CardContent, CardHeader, CardTitle } from '@/components/ui/card';
import { useAuth } from '@/contexts/AuthContext';

const Signup = () => {
  const navigate = useNavigate();
  const { login } = useAuth();

  const [ngoName, setNgoName] = useState('');
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const [error, setError] = useState('');

  const handleSignup = (e: React.FormEvent) => {
    e.preventDefault();

    if (!ngoName || !email || !password) {
      setError('All fields are required');
      return;
    }

    // 🔹 Dummy user object (frontend only)
    const newUser = {
      email,
      ngo_name: ngoName,
      password, // stored only for demo
    };

    // Save to localStorage
    localStorage.setItem('dummyAccount', JSON.stringify(newUser));

    // Auto-login after signup
    login(email, password);

    navigate('/dashboard');
  };

  return (
    <div className="min-h-screen flex items-center justify-center bg-background">
      <Card className="w-full max-w-md">
        <CardHeader>
          <CardTitle>Create NGO Account</CardTitle>
        </CardHeader>

        <CardContent>
          <form onSubmit={handleSignup} className="space-y-4">
            <div className="space-y-2">
              <Label>NGO Name</Label>
              <Input
                value={ngoName}
                onChange={(e) => setNgoName(e.target.value)}
                placeholder="Demo NGO"
              />
            </div>

            <div className="space-y-2">
              <Label>Email</Label>
              <Input
                value={email}
                onChange={(e) => setEmail(e.target.value)}
                placeholder="demo@ngo.com"
              />
            </div>

            <div className="space-y-2">
              <Label>Password</Label>
              <Input
                type="password"
                value={password}
                onChange={(e) => setPassword(e.target.value)}
                placeholder="password123"
              />
            </div>

            {error && (
              <p className="text-sm text-red-500">{error}</p>
            )}

            <Button type="submit" className="w-full">
              Create Account
            </Button>

            <p className="text-xs text-muted-foreground text-center">
              Already have an account?{' '}
              <Link to="/auth" className="text-primary underline">
                Login
              </Link>
            </p>
          </form>
        </CardContent>
      </Card>
    </div>
  );
};

export default Signup;
