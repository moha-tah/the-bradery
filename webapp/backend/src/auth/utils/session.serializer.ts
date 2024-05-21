import { Injectable } from '@nestjs/common';
import { PassportSerializer } from '@nestjs/passport';
import { UsersService } from '../../users/users.service';
import { User } from 'src/users/types';

@Injectable()
export class SessionSerializer extends PassportSerializer {
  constructor(private readonly usersService: UsersService) {
    super();
  }

  serializeUser(user: User, done: (err: Error, userId: number | null) => void) {
    done(null, user.id);
  }

  async deserializeUser(id: number, done: (err: Error, user: User) => void) {
    const user = await this.usersService.findUserById(id);

    if (!user) {
      done(
        {
          name: 'DeserializeError',
          message: `Could not deserialize user: user with ${id} could not be found`,
        } as Error,
        null,
      );
      return;
    }

    done(null, user);
  }
}
