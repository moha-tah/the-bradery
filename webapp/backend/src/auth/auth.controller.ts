import {
  Body,
  ConflictException,
  Controller,
  Get,
  InternalServerErrorException,
  Post,
  Req,
  UseGuards,
} from '@nestjs/common';
import { Request } from 'express';
import { UsersService } from 'src/users/users.service';
import { IsAuthenticatedGuard } from './decorators/guards/is-authenticated.guard';
import { LocalAuthGuard } from './decorators/guards/local-auth.guard';
import { AuthDTO } from './dto/auth.dto';
import { LoginResponse, LogoutResponse, SignUpResponse } from 'src/auth/types';
import { User } from 'src/users/types';

@Controller('api/auth')
export class AuthController {
  constructor(private readonly userService: UsersService) {}

  @Post('signup')
  async register(@Body() dto: AuthDTO, @Req() request: Request) {
    if (await this.userService.findUserByEmail(dto.email))
      throw new ConflictException('User already exists');
    try {
      const user = await this.userService.registerUser(dto.email, dto.password);

      await new Promise((resolve, reject) => {
        request.logIn(user, (err) => {
          if (err) {
            reject(err);
          } else {
            resolve(user);
          }
        });
      });

      const response: SignUpResponse = {
        redirectTo: '/shop',
      };
      return response;
    } catch (error) {
      throw new InternalServerErrorException('Could not register user');
    }
  }

  @UseGuards(LocalAuthGuard)
  @Post('login')
  async login(@Req() request: Request) {
    const response: LoginResponse = {
      redirectTo: '/shop',
      user: request.user as User,
    };
    return response;
  }

  @UseGuards(IsAuthenticatedGuard)
  @Get('logout')
  async logout(@Req() request: Request) {
    const logoutError = await new Promise((resolve) =>
      request.logOut({ keepSessionInfo: false }, (error) => resolve(error)),
    );

    if (logoutError)
      throw new InternalServerErrorException('Could not log out user');

    const response: LogoutResponse = {
      logout: true,
    };

    return response;
  }
}
