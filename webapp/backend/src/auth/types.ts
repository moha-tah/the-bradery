import { User } from 'src/users/types';

export type SignUpResponse = {
  redirectTo: string;
};

export type LoginResponse = {
  redirectTo: string;
  user: User;
};

export type LogoutResponse = {
  logout: boolean;
};
