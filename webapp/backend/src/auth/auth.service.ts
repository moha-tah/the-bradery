import { Injectable, UnauthorizedException } from '@nestjs/common';
import { User } from 'src/users/types';
import { UsersService } from 'src/users/users.service';

@Injectable()
export class AuthService {
  constructor(private readonly usersService: UsersService) {}

  async validateUser(email: string, password: string): Promise<User> {
    const user = await this.usersService.findUserByEmail(email);
    if (!user) throw new UnauthorizedException({ mailFailed: true });

    // const passwordValid = await bcrypt.compare(
    //   password,
    //   passwordHash,
    // );
    // if (!passwordValid) throw new UnauthorizedException({ mailFailed: false });

    return user;
  }
}
